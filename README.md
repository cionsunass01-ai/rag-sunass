# RAG Documental SUNASS

Procesamiento batch de expedientes en PDF para extraer 28 variables y
generar JSONs usando FAISS + BGE-M3 (sin LLM).

## Requisitos

### Sistema
- `tesseract-ocr` (con idioma `spa`)
- `poppler-utils`

### Python
```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py --input ./pdfs --output ./resultados [--consolidar]
```

- `--input` carpeta con PDFs.
- `--output` carpeta de salida (creada si no existe).
- `--consolidar` (opcional) genera un `consolidado.json`.

El primer arranque descarga el modelo BGE-M3 (~2.2 GB).
