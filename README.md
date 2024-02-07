# Email Sending Application

This project encompasses three different methods of sending emails using Python: sending emails via Gmail API, sending emails via SMTP server, and obtaining access token for Gmail API using a script.

## Files and Usage

- `send_mail_with_gmail.py`: This file contains a Python script to send emails using Gmail API. The `send_gmail_message` function sends a specific message with a specific subject to a specific recipient.

  - Usage: `send_gmail_message("message text", "subject")`

- `token_extract_for_gmail.py`: This script is used to obtain access token for Gmail API. It relies on environment variables such as `credentials_file_path`, `token_file_path`, and `scopes`.

- `send_mail_with_smtplib.py`: This file contains a Python script to send emails using SMTP server. The `send_email` function sends an email with a specific subject and message to a specific recipient.

  - Usage: `send_email("subject", "message text")`

## Environment Variables

This application requires environment variables to read various information. These information are read from a `.env` file using the `dotenv` module.

- `sender_email`: Sender's email address.
- `recipient_email`: Recipient's email address.
- `credentials_file_path`: File path containing authentication credentials for Gmail API access token.
- `token_file_path`: File path where the access token will be saved.
- `scopes`: Scopes for Gmail API access.
- `email_key`: Email key for SMTP server authentication.

## Installation

1. Install Python 3 and pip.
2. Download or clone the project folder.
3. Install the requirements listed in the `requirements.txt` file by running `pip install -r requirements.txt` in your terminal or command prompt.
4. Create a `.env` file and specify the environment variables mentioned above.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
