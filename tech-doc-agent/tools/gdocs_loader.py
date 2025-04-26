import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def authenticate():
    creds = None
    token_path = 'token.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            auth_url, _ = flow.authorization_url(prompt='consent')
            print(f'👉 Authorize here:\n{auth_url}')
            code = input('🔑 Enter the authorization code here: ').strip()
            flow.fetch_token(code=code)
            creds = flow.credentials

        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds

def get_doc_text(doc_id):
    creds = authenticate()
    service = build('docs', 'v1', credentials=creds)
    document = service.documents().get(documentId=doc_id).execute()
    
    # Assuming you want to extract text from the document
    doc_content = document.get('body', {}).get('content', [])
    
    text = ''
    for element in doc_content:
        paragraph = element.get('paragraph')
        if paragraph:
            for elem in paragraph.get('elements', []):
                text_run = elem.get('textRun')
                if text_run:
                    text += text_run.get('content', '')
    
    return text
