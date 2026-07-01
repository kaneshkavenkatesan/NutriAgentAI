import os
import requests

def send_email(receiver_email, subject, message):

    print("===== EMAIL FUNCTION STARTED =====")

    api_key = os.environ.get("BREVO_API_KEY")
    print("API KEY FOUND:", api_key is not None)

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
        <h2>NutriAgent AI</h2>
        <pre>{message}</pre>
        """
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)
    print("===== EMAIL FUNCTION FINISHED =====")