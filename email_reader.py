# File: email_reader.py

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import base64

# Scopes required to read and send emails
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    creds = None
    # MANUAL: Place 'credentials.json' from Google Developer Console in project root
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)  # Opens browser for OAuth
    service = build('gmail', 'v1', credentials=creds)
    return service
  
  # File: email_reader.py (continued)



def get_unread_emails(service):
    # Fetch unread emails from inbox
    result = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
    messages = result.get('messages', [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data['payload']
        headers = payload['headers']

        # Extract subject and sender
        subject = [h['value'] for h in headers if h['name'] == 'Subject'][0]
        sender = [h['value'] for h in headers if h['name'] == 'From'][0]

        # Get body content
        parts = payload.get('parts', [])
        if parts:
            body_data = parts[0]['body']['data']
        else:
            body_data = payload['body']['data']
        body = base64.urlsafe_b64decode(body_data).decode('utf-8')
        clean_body = BeautifulSoup(body, 'html.parser').text

        emails.append({
            'id': msg['id'],
            'subject': subject,
            'sender': sender,
            'body': clean_body
        })

    return emails