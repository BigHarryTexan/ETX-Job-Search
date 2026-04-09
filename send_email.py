import os
import json
import base64
import requests

SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]

def send_email():
    # Read the weekly report content
    with open("weekly_report.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Read the file again for attachment (binary-safe)
    with open("weekly_report.md", "rb") as f:
        attachment_bytes = f.read()
        attachment_b64 = base64.b64encode(attachment_bytes).decode()

    # Build the SendGrid payload
    data = {
        "personalizations": [
            {
                "to": [{"email": "clayharryman@gmail.com"}],
                "subject": "ETX Job Watch Report"
            }
        ],
        "from": {"email": "clayharryman@gmail.com"},
        "content": [
            {
                "type": "text/plain",
                "value": "Your weekly ETX Job Watch Report is attached.\n\n"
                         "This email includes:\n"
                         "- Clean URLs (no tracking)\n"
                         "- Full Markdown report as an attachment\n"
            }
        ],
        "attachments": [
            {
                "content": attachment_b64,
                "type": "text/markdown",
                "filename": "weekly_report.md",
                "disposition": "attachment"
            }
        ],
        "tracking_settings": {
            "click_tracking": {
                "enable": False,
                "enable_text": False
            }
        }
    }

    # Send the email
    r = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps(data)
    )

    print("Status:", r.status_code)
    print("Response:", r.text)

if __name__ == "__main__":
    send_email()
