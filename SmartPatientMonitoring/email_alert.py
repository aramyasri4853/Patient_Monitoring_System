import smtplib
from email.mime.text import MIMEText

# Your email
SENDER_EMAIL = "xxxxxxxxxxx@gmail.com"
APP_PASSWORD = "xxxxxxxxxxxxxxxxxxxx"
RECEIVER_EMAIL = "xxxxxxxxxx@gmail.com"


def send_email_alert(message):

    try:
        msg = MIMEText(message)
        msg["Subject"] = "🚨 Patient Emergency Alert"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)

        server.send_message(msg)
        server.quit()

        print("📩 Email sent successfully!")

    except Exception as e:
        print("Email error:", e)
