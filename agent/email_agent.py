import os
import requests


def send_email(receiver_email, subject, message):
    print("BREVO EMAIL FUNCTION CALLED")

    api_key = os.environ.get("BREVO_API_KEY")

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }

    data = {
        "sender": {
            "name": "NutriAgent AI",
            "email": "kaneshkavenkat@gmail.com"
        },
        "to": [
            {
                "email": receiver_email
            }
        ],
        "subject": subject,
        "htmlContent": f"""
        <html>
        <body>
            <h2>NutriAgent AI</h2>

            <pre style="font-size:16px;">
{message}
            </pre>

        </body>
        </html>
        """
    }

    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    print(response.status_code)
    print(response.text)