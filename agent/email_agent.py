import smtplib

from email.mime.text import MIMEText


def send_email(
    receiver_email,
    subject,
    message
):

    sender_email = "kaneshkavenkat@gmail.com"

    app_password = "jhwl ylvw rvdo utmw"

    msg = MIMEText(message)

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            sender_email,
            app_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print("Email Sent Successfully")

    except Exception as e:

        print("Email Error:", e)