import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def get_drive_service():
    credentials_data = json.loads(
        os.getenv("GOOGLE_CREDENTIALS_JSON")
    )

    credentials = service_account.Credentials.from_service_account_info(
        credentials_data,
        scopes=SCOPES
    )

    service = build(
        "drive",
        "v3",
        credentials=credentials
    )

    return service
