# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


message = Mail(
    from_email=os.environ.get('SENDGRID_SENDER_MAIL'),
    to_emails=os.environ.get('SENDGRID_RECIPIENT_MAIL'),
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

print(message)

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
print(sg.api_key)
print(sg)
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)

