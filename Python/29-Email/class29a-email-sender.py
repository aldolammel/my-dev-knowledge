"""
SENDING EMAIL


"""

import smtplib
from email.mime.text import MIMEText  # Encoding UTF-8

# Constant:
FROM_SENDER = "aldolammel@gmail.com"
SENDER_PASS = "bvcnmmqrxpkymvcl"  # https://myaccount.google.com/security >> "App passwords"
SENDER_SMTP = "smtp.gmail.com"
SMTP_PORT = 587
TO_RECEIVER = "aldolammel@hotmail.com"
SUBJECT = "Hello world"

body = "This is the body of my email. Characters tester: Çáéüô."
body_encoded = MIMEText(body, "plain")  # Encoding UTF-8 for Python 3

with smtplib.SMTP(SENDER_SMTP, port=SMTP_PORT) as connection:
    connection.starttls()
    connection.login(user=FROM_SENDER, password=SENDER_PASS)
    connection.sendmail(
        from_addr=FROM_SENDER,
        to_addrs=TO_RECEIVER,
        msg=f"Subject: {SUBJECT}\n{body_encoded.as_string()}")
