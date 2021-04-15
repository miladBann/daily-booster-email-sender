import smtplib
from email.message import EmailMessage
import random
import datetime as dt

now = dt.datetime.now()
today = now.weekday()

if today == 0 or today == 1 or today == 2 or today == 3 or today == 4 or today == 5 or today == 6:
    with open("quotes.txt", mode="r") as data_file:
        text = data_file.readlines()
        todays_quote = random.choice(text)

        email = EmailMessage()
        email["from"] = "Daily Inspiration"
        email["to"] = "miladbannourah@outlook.com"
        email["Subject"] = "Boost of the day"
        email.set_content(todays_quote)

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("hstevejobs@gmail.com", "milomilo2002")
            smtp.send_message(email)
            print("email sent")
