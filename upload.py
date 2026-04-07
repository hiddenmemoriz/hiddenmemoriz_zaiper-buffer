import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Load credentials from environment variable
service_account_info = json.loads(os.environ['GDRIVE_SERVICE_ACCOUNT'])
credentials = service_account.Credentials.from_service_account_info(service_account_info)

drive_service = build('drive', 'v3', credentials=credentials)

folder_id = '1EVIHk24_3C7DsCLcYoQOdrM_T11UrkWH'
file_metadata = {
    'name': 'spotify.png',
    'parents': [folder_id]
}

media = MediaFileUpload('spotify.png', mimetype='image/png')

try:
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(f"File ID: {file.get('id')} uploaded successfully.")
except Exception as e:
    print(f"Error: {e}")
    exit(1)
