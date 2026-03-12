# rag_sunass/main.py

import os
import glob
import json
import argparse
from datetime import datetime

import torch

from embeddings import BGEM3Embeddings, MODEL_NAME
from cuestionario import CUESTIONARIO_SUNASS
from pdf_processing import cargar_pdf
from retrieval import (
    recuperar_contextos,
    recuperar_contextos_encabezado,
    N_FRASES,
)
from json_builder import generar_json


def procesar_batch(
    carpeta_input: str,
    carpeta_output: str,
    consolidar: bool,
    embeddings_model: BGEM3Embeddings,
) -> None:
    """
    Procesa todos los PDFs en carpeta_input y guarda un JSON por cada uno
    en carpeta_output. Si consolidar=True, también genera consolidado.json.
    """
    os.makedirs(carpeta_output, exist_ok=True)

    pdfs = sorted(glob.glob(os.path.join(carpeta_input, "**", "*.pdf"), recursive=True))
    if not pdfs:
        print(f"❌ No se encontraron PDFs en: {carpeta_input}")
        return

    print(f"\n📂 PDFs encontrados: {len(pdfs)}")
    print(f"📁 Salida           : {carpeta_output}\n")

    jsons_generados = []

    for idx, pdf_path in enumerate(pdfs, 1):
        pdf_fn = os.path.basename(pdf_path)
        sep = "═" * 60
        print(f"\n{sep}")
        print(f"  [{idx}/{len(pdfs)}]  {pdf_fn}")
        print(sep)

        try:
            vs, texto_completo = cargar_pdf(pdf_path, embeddings_model)
        except ValueError as e:
            print(f"  ❌ Error cargando PDF: {e}\n  Se omite este archivo.")
            continue

        resultados = []
        bloque_prev = None

        for item in CUESTIONARIO_SUNASS:
            if item["bloque"] != bloque_prev:
                bloque_prev = item["bloque"]
                print(f"\n  📁 {item['bloque']}")
                print("  " + "─" * 48)

            ctxs = (
                recuperar_contextos_encabezado(texto_completo, item, 2)
                if item.get("es_encabezado")
                else recuperar_contextos(vs, item, N_FRASES)
            )

            resultados.append({
                "id"         : item["id"],
                "bloque"     : item["bloque"],
                "variable"   : item["variable"],
                "descripcion": item["descripcion"],
                "contextos"  : ctxs,
            })

            icon    = "✅" if ctxs else "⚠️ "
            preview = f'"{ctxs[0][:65]}..."' if ctxs else "Sin contexto"
            print(f"  {icon} [{item['id']:02d}] {item['variable']:<28} → {preview}")

        rj   = generar_json(pdf_fn, resultados)
        n_ok = rj["metadata"]["variables_con_contexto"]
        tot  = rj["metadata"]["total_variables"]
        pct  = rj["metadata"]["cobertura_pct"]

        ts        = datetime.now().strftime("%Y%m%d_%H%M%S")
        base      = os.path.splitext(pdf_fn)[0]
        ruta_json = os.path.join(carpeta_output, f"{base}_{ts}.json")

        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(rj, f, ensure_ascii=False, indent=2)

        jsons_generados.append(ruta_json)
        print(f"\n  💾 {ruta_json}")
        print(f"  📊 Cobertura: {n_ok}/{tot} variables ({pct}%)")

    # ── Consolidado ────────────────────────────────────────────────────
    if consolidar and jsons_generados:
        consolidado = []
        for ruta in jsons_generados:
            with open(ruta, encoding="utf-8") as f:
                consolidado.append(json.load(f))

        ruta_cons = os.path.join(carpeta_output, "consolidado.json")
        with open(ruta_cons, "w", encoding="utf-8") as f:
            json.dump(consolidado, f, ensure_ascii=False, indent=2)
        print(f"\n📦 Consolidado: {ruta_cons}  ({len(consolidado)} expedientes)")

    print(f"\n✅ Batch completo — {len(jsons_generados)}/{len(pdfs)} documentos procesados")


# ══════════════════════════════════════════════════════════════════════
#  ENTRYPOINT
# ══════════════════════════════════════════════════════════════════════


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RAG SUNASS — Extracción batch de 28 variables a JSON",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Carpeta con los PDFs de expedientes a procesar",
    )
    parser.add_argument(
        "--output", "-o",
        default="./resultados",
        help="Carpeta donde se guardan los JSONs (default: ./resultados)",
    )
    parser.add_argument(
        "--consolidar", "-c",
        action="store_true",
        help="Genera además un archivo consolidado.json con todos los resultados",
    )
    parser.add_argument(
        "--device",
        default=None,
        help="Dispositivo: 'cpu' o 'cuda' (auto-detecta si no se especifica)",
    )
    args = parser.parse_args()

    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n⏳ Cargando BGE-M3 en {device}  (primera descarga ~2.2 GB)...")
    embeddings_model = BGEM3Embeddings(model_name=MODEL_NAME, device=device)
    test = embeddings_model.embed_query("prueba")
    print(f"✅ BGE-M3 listo — dim: {len(test)}  ctx: 8192 tokens")

    procesar_batch(
        carpeta_input   = args.input,
        carpeta_output  = args.output,
        consolidar      = args.consolidar,
        embeddings_model= embeddings_model,
    )


if __name__ == "__main__":
    main()
