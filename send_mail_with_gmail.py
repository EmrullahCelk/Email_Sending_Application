from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
from os import getenv
import json
import base64

load_dotenv()

def send_gmail_message(message_text, subject):

    sender_email = getenv("sender_email")
    recipient_email = getenv("recipient_email")
    credentials_file_path = getenv("credentials_file_path")
    token_file_path = getenv("token_file_path")

    with open(token_file_path, "r") as token_file:
        token_data = json.load(token_file)

    # Retrieve the 'scopes' information from the 'scopes' field in the token.json file.
    scopes_from_token = token_data.get("scopes", [])

    # Create the Credentials object
    credentials = Credentials.from_authorized_user_file(token_file_path, scopes=scopes_from_token)

    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
                 credentials_file_path, scopes_from_token)
        credentials = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    service = build('gmail', 'v1', credentials=credentials)

    message = MIMEText(message_text , 'plain')
    message['to'] = recipient_email
    message['from'] = sender_email
    message['subject'] = subject 

    message = service.users().messages().send(userId='me', body={'raw': base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")}).execute()
 
    print("E-posta gönderildi.")



send_gmail_message("test message", "test")

