import os
from dotenv import load_dotenv
from app.utils.auth import get_drive_service

load_dotenv()

FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")


def search_drive(query):
    service = get_drive_service()

    response = service.files().list(
        q=f"'{FOLDER_ID}' in parents and {query}",
        fields="files(id,name,mimeType,webViewLink,modifiedTime)"
    ).execute()

    return response.get("files", [])
