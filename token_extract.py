import os
from google_auth_oauthlib.flow import InstalledAppFlow

# Credential dosyanızın yolu
credential_path = 'C:\\Users\\i7\Documents\\GitHub\\Send_Mail_With_smtplib\\credendials.json'

# Token dosyanızın yolu
token_path = 'C:\\Users\\i7\\Documents\\GitHub\\Send_Mail_With_smtplib\\token.json'

# API kapsamını belirtin (örneğin, 'https://www.googleapis.com/auth/gmail.readonly')
scopes = ['https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.readonly',
          'https://mail.google.com/']

# Token dosyanız yoksa kimlik doğrulama akışını başlatın
flow = InstalledAppFlow.from_client_secrets_file(credential_path, scopes)
credentials = flow.run_local_server(port=0)

# Token'ı kaydet
os.makedirs(os.path.dirname(token_path), exist_ok=True)
with open(token_path, 'w') as token:
    token.write(credentials.to_json())
