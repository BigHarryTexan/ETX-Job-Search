import os
import json
import requests

SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]

def send_email():
    # Read the weekly report content
    with open("weekly_report.md", "r", encoding="utf-8") as f:
        content = f.read()

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
                "value": content
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
