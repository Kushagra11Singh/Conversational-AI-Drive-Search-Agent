import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE"),
        scopes=SCOPES
    )

    service = build(
        "drive",
        "v3",
        credentials=credentials
    )

    return service
