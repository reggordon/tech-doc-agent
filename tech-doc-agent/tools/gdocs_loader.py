from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_doc_text(doc_id):
    creds = authenticate()
    service = build('docs', 'v1', credentials=creds)
    document = service.documents().get(documentId=doc_id).execute()

    text = ""
    for element in document.get("body", {}).get("content", []):
        if "paragraph" in element:
            for elem in element["paragraph"]["elements"]:
                text += elem.get("textRun", {}).get("content", "")
    return text
