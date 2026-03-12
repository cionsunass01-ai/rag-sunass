# rag_sunass/json_builder.py

from datetime import datetime

from retrieval import MMR_K, MMR_FETCH_K, MMR_LAMBDA


def generar_json(nombre_doc: str, resultados: list) -> dict:
    """Construye el dict JSON con metadata + 28 variables."""
    n_ok = sum(1 for r in resultados if r["contextos"])
    total = len(resultados)
    return {
        "metadata": {
            "documento"             : nombre_doc,
            "procesado"             : datetime.now().isoformat(timespec="seconds"),
            "metodo"                : "RAG semantico — FAISS + BAAI/bge-m3 — sin LLM",
            "modelo_embeddings"     : "BAAI/bge-m3",
            "parametros_retrieval"  : {
                "mmr_k": MMR_K, "fetch_k": MMR_FETCH_K, "lambda_mult": MMR_LAMBDA
            },
            "total_variables"       : total,
            "variables_con_contexto": n_ok,
            "cobertura_pct"         : round(n_ok / total * 100, 1),
        },
        "variables": {
            r["variable"]: {
                "id"         : r["id"],
                "bloque"     : r["bloque"],
                "descripcion": r["descripcion"],
                "contextos"  : r["contextos"],
            }
            for r in resultados
        },
    }
