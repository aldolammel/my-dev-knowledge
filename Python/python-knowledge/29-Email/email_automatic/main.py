import datetime as dt
import random
import pandas as pd
import smtplib

# Initial values:
is_birthday_someone = False
# Constants:
FROM_SENDER = "aldolammel@gmail.com"
SENDER_PASS = "wppunpwhomlwquyk"  # https://myaccount.google.com/security >> 2-Factor >> "App passwords"
SENDER_SMTP = "smtp.gmail.com"
SMTP_PORT = 587
TO_RECEIVER = "aldolammel@hotmail.com"
TEMPLATES_NUMBER = 3
# Today:
today = dt.datetime.now()
day = 30  # today.day <------------ TO TEST CHANGE IT!
month = today.month  # today.month <------ TO TEST CHANGE IT!
year = today.year
# Birthdays
database = pd.read_csv("birthdays.csv")
# Check if someone birthday:
database_dict = database.to_dict(orient="records")  # organizing by entry and not by column.

for person in database_dict:
    if person["day"] == day and person["month"] == month:
        # flag:
        is_birthday_someone = True
        # message:
        print(f"Today is {person['name']} birthday!")
        # Preparing the letter:
        with open(f"letter_templates/letter_{random.randint(1,TEMPLATES_NUMBER)}.txt", mode="r") as file_template:
            template = file_template.read()
            customized_email = template.replace("[NAME]", person["name"])
            # Writing the customized letter and storage it:
            with open(f"output/{year}_{person['name'].lower()}.txt", mode="w") as file_ready:
                file_ready.write(customized_email)
            print(f">> {person['name']} birthday's email has been created and storage as txt file.")
        # Sending email:
        with smtplib.SMTP(SENDER_SMTP, port=SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=FROM_SENDER, password=SENDER_PASS)
            connection.sendmail(
                from_addr=FROM_SENDER,
                to_addrs=TO_RECEIVER,
                msg=f"Subject: Happy birthday, {person['name']}!\n\n{customized_email}")

if not is_birthday_someone:
    print("Today is NOT the birthday of anyone.")

print("The birthday email sender has been finished for today.")
