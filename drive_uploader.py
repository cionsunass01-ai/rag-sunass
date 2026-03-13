# rag_sunass/drive_uploader.py

import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def subir_resultados():
    folder_id = os.getenv("DRIVE_RESULTS_FOLDER_ID")
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    refresh_token = os.getenv("GOOGLE_REFRESH_TOKEN")

    if not all([folder_id, client_id, client_secret, refresh_token]):
        raise ValueError("Faltan variables de entorno para Google Drive.")

    creds = Credentials(
        None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
    )

    service = build("drive", "v3", credentials=creds)

    carpeta_local = "resultados"

    if not os.path.exists(carpeta_local):
        print("No existe carpeta resultados.")
        return

    archivos = [f for f in os.listdir(carpeta_local) if f.endswith(".json")]

    if not archivos:
        print("No hay JSON para subir.")
        return

    print(f"📤 Subiendo {len(archivos)} archivos a Drive...")

    for archivo in archivos:
        ruta = os.path.join(carpeta_local, archivo)

        media = MediaFileUpload(
            ruta,
            mimetype="application/json",
            resumable=True
        )

        file_metadata = {
            "name": archivo,
            "parents": [folder_id]
        }

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()

        print(f"✅ Subido: {archivo}")

    print("🎉 Subida completa.")


if __name__ == "__main__":
    subir_resultados()