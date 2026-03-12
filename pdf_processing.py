# rag_sunass/pdf_processing.py

from typing import List
import fitz
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf2image import convert_from_path
import pytesseract
from langchain_community.vectorstores import FAISS

from embeddings import BGEM3Embeddings

OCR_THRESHOLD = 50   # chars/página — por debajo se aplica Tesseract
CHUNK_SIZE = 600
CHUNK_OVERLAP = 80


def extraer_texto_nativo(pdf_path: str) -> List[Document]:
    """Extrae texto seleccionable con PyMuPDF."""
    docs = []
    pdf = fitz.open(pdf_path)
    for i, page in enumerate(pdf):
        text = page.get_text().strip()
        if text:
            docs.append(Document(
                page_content=text,
                metadata={"source": pdf_path, "page": i + 1, "metodo": "nativo"},
            ))
    pdf.close()
    return docs


def extraer_texto_ocr(pdf_path: str) -> List[Document]:
    """Aplica Tesseract OCR en español para PDFs escaneados."""
    print("    🔍 PDF escaneado — aplicando OCR (Tesseract spa, dpi=300)...")
    imagenes = convert_from_path(pdf_path, dpi=300, fmt="png")
    docs = []
    for i, img in enumerate(imagenes):
        text = pytesseract.image_to_string(
            img, lang="spa", config="--oem 3 --psm 6"
        ).strip()
        if text:
            docs.append(Document(
                page_content=text,
                metadata={"source": pdf_path, "page": i + 1, "metodo": "ocr"},
            ))
        print(f"      📷 Pág {i+1}/{len(imagenes)} — {len(text)} chars")
    return docs


def cargar_pdf(pdf_path: str, embeddings_model: BGEM3Embeddings) -> tuple:
    """
    Carga el PDF, aplica OCR si es necesario y construye el índice FAISS.
    Retorna (vectorstore, texto_completo).
    """
    docs = extraer_texto_nativo(pdf_path)
    cpp = sum(len(d.page_content) for d in docs) / max(len(docs), 1)

    print(f"    📄 Páginas: {len(docs)}  |  chars/pág: {cpp:.0f}", end="")

    if cpp < OCR_THRESHOLD:
        docs = extraer_texto_ocr(pdf_path)
        print(f"  →  OCR ({len(docs)} págs)")
    else:
        print("  →  texto nativo")

    if not docs:
        raise ValueError("No se pudo extraer texto del PDF.")

    texto_completo = "\n\n".join(d.page_content for d in docs)

    from langchain_text_splitters import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " "],
    )
    chunks = splitter.split_documents(docs)
    print(f"    ✂️  Chunks: {len(chunks)}")

    if not chunks:
        raise ValueError("No se generaron chunks.")

    vs = FAISS.from_documents(chunks, embeddings_model)
    return vs, texto_completo
