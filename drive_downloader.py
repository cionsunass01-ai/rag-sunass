# rag_sunass/drive_downloader.py

import os
import io
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def descargar_pdfs():
    folder_id = os.getenv("DRIVE_FOLDER_ID")
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    refresh_token = os.getenv("GOOGLE_REFRESH_TOKEN")

    if not all([folder_id, client_id, client_secret, refresh_token]):
        raise ValueError("Faltan variables de entorno para Google Drive.")

    # Crear credenciales usando refresh token (igual que TanIA)
    creds = Credentials(
        None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
    )

    service = build("drive", "v3", credentials=creds)

    # Crear carpeta local ./pdfs
    os.makedirs("pdfs", exist_ok=True)

    print(f"📂 Buscando PDFs en carpeta Drive: {folder_id}")

    query = f"'{folder_id}' in parents and mimeType='application/pdf' and trashed=false"

    results = service.files().list(
        q=query,
        fields="files(id, name)"
    ).execute()

    files = results.get("files", [])

    if not files:
        print("⚠️ No se encontraron PDFs en Drive.")
        return

    for file in files:
        file_id = file["id"]
        file_name = file["name"]

        print(f"⬇ Descargando: {file_name}")

        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(f"pdfs/{file_name}", "wb")
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        print(f"✅ Descargado: {file_name}")

    print(f"\n🎉 Descarga completa — {len(files)} archivos")


if __name__ == "__main__":
    descargar_pdfs()