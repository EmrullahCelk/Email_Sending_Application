import smtplib
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def send_gmail_message(message_text, subject):

    SCOPES = getenv("SCOPES")
    sender_email = getenv("sender_email")
    recipient_email = getenv("recipient_email")
    credentials_file_path = getenv("credentials_file_path")

    credentials = Credentials.from_authorized_user_file(credentials_file_path, scopes=SCOPES)

    message = MIMEText(message_text , 'plain')
    message['to'] = recipient_email
    message['from'] = sender_email
    message['subject'] = subject 
    
    # Gmail SMTP sunucu bilgileri
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # SMTP bağlantısı oluştur
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # TLS bağlantısı başlat
        server.starttls()

        # OAuth 2.0 ile kimlik doğrulaması yap
        server.ehlo()
        credentials.refresh(Request())
        server.login(sender_email, credentials.token)  # Parola gerekli değil

        # E-postayı gönder
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("E-posta gönderildi.")



send_gmail_message("deneme mesaji", "deneme")