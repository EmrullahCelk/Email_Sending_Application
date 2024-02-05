import os
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv


load_dotenv()

credential_path = os.getenv("credentials_file_path")
token_path = os.getenv("token_file_path")
scopes = os.getenv("scopes")


flow = InstalledAppFlow.from_client_secrets_file(credential_path, scopes)
credentials = flow.run_local_server(port=0)

# save token
os.makedirs(os.path.dirname(token_path), exist_ok=True)
with open(token_path, 'w') as token:
    token.write(credentials.to_json())
