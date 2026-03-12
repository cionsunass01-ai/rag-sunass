# retrieval.py

import re
from typing import List

# parámetros de retrieval
MMR_K = 6
MMR_FETCH_K = 20
MMR_LAMBDA = 0.6
N_FRASES = 2  # fragmentos de contexto por variable


def limpiar_texto(texto: str) -> str:
    texto = re.sub(r"\s+", " ", texto)
    texto = re.sub(r"[|]{2,}", "", texto)
    texto = re.sub(r"\.{3,}", "...", texto)
    return texto.strip()


def fragmentar_en_frases(texto: str, min_chars: int = 30) -> List[str]:
    candidatos = re.split(r"(?<=[.;])\s+|\n", texto)
    return [f.strip() for f in candidatos if len(f.strip()) >= min_chars]


def score_frase(frase: str, keywords: List[str]) -> float:
    fl = frase.lower()
    return sum(1 for kw in keywords if kw.lower() in fl)


def recuperar_contextos(vectorstore, item: dict, n_frases: int = N_FRASES) -> List[str]:
    """Recupera fragmentos relevantes vía MMR + scoring por keywords."""
    docs = vectorstore.max_marginal_relevance_search(
        item["query_busqueda"],
        k=MMR_K,
        fetch_k=MMR_FETCH_K,
        lambda_mult=MMR_LAMBDA,
    )
    texto = " ".join(limpiar_texto(d.page_content) for d in docs)
    frases = fragmentar_en_frases(texto)

    if not frases:
        return []

    scored = sorted(
        [(f, score_frase(f, item["keywords"])) for f in frases],
        key=lambda x: x[1],
        reverse=True,
    )

    seleccionadas: List[str] = []
    for frase, _ in scored:
        es_dup = any(
            frase[:40].lower() in ya.lower() or ya[:40].lower() in frase.lower()
            for ya in seleccionadas
        )
        if not es_dup:
            seleccionadas.append(frase[:300] + ("..." if len(frase) > 300 else ""))
        if len(seleccionadas) >= n_frases:
            break

    return seleccionadas


def recuperar_contextos_encabezado(
    texto_completo: str, item: dict, n_frases: int = 2
) -> List[str]:
    """Para CUTF y SISTRAM_ID: busca en los primeros 2500 chars del documento."""
    frases = fragmentar_en_frases(texto_completo[:2500], min_chars=15)
    if not frases:
        return []

    scored = sorted(
        [(f, score_frase(f, item["keywords"])) for f in frases],
        key=lambda x: x[1],
        reverse=True,
    )

    seleccionadas: List[str] = []
    for frase, _ in scored:
        if not any(frase[:40].lower() in ya.lower() for ya in seleccionadas):
            seleccionadas.append(frase[:300] + ("..." if len(frase) > 300 else ""))
        if len(seleccionadas) >= n_frases:
            break

    return seleccionadas
