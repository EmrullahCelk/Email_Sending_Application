import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
from os import getenv


load_dotenv()


def send_email(subject, body):
    # Gönderen e-posta bilgileri
    from_email = getenv("sender_email")
    email_key = getenv("email_key")
    to_email = getenv("recipient_email")

    # E-posta oluşturma
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # E-posta gövdesi
    msg.attach(MIMEText(body, 'plain'))

    # SMTP sunucusuna bağlanma
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, email_key)

        # E-posta gönderme
        server.sendmail(from_email, to_email, msg.as_string())

# Örnek kullanım
subject = "test mail"
body = "test mail"


send_email(subject, body)