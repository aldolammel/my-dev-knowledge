from flask import Flask, render_template, request
import requests
import smtplib
from email.mime.text import MIMEText  # Encoding UTF-8
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# BLOG POSTS:
ENDPOINT = "https://api.npoint.io/db0d95975a4e724bcb1c"
all_posts = requests.get(url=ENDPOINT).json()

# SMTPLIB:
FROM_SENDER = os.environ["FROM_SENDER"]  # email gmail
SENDER_PASS = os.environ["SENDER_PASS"]  # myaccount.google.com/security >> 2-Step Verification >> App passwords
SENDER_SMTP = "smtp.gmail.com"
SMTP_PORT = 587
TO_RECEIVER = "aldolammel@hotmail.com"
SUBJECT = "Contact from blog"


@app.route("/")
def get_home():
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def go_contact():
    msg_sent = False
    if request.method == "POST":
        data = request.form
        msg_sent = send_email(data["name"], data["email"], data["phone"], data["message"])
    return render_template("contact.html", msg_sent=msg_sent)


def send_email(user_name, user_email, user_phone, user_message):
    body = f"{user_name}\n{user_email}\n{user_phone}\n{user_message}"
    body_encoded = MIMEText(body, "plain")  # Encoding UTF-8 for Python 3

    with smtplib.SMTP(SENDER_SMTP, port=SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=FROM_SENDER, password=SENDER_PASS)
        connection.sendmail(
            from_addr=FROM_SENDER,
            to_addrs=TO_RECEIVER,
            msg=f"Subject: {SUBJECT}\n{body_encoded.as_string()}")
    return True


@app.route("/post/<int:post_id>")
def get_post(post_id):
    for blog_post in all_posts:
        if blog_post["id"] == post_id:
            return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # This IP is a special that force Flask to run in all machines with app access.
