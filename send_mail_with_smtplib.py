import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
from os import getenv


load_dotenv()


def send_email(subject, body):

    from_email = getenv("sender_email")
    email_key = getenv("email_key")
    to_email = getenv("recipient_email")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject


    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, email_key)


        server.sendmail(from_email, to_email, msg.as_string())


subject = "test"
body = "test message"


send_email(subject, body)