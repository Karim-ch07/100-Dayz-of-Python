from smtplib import *
from datetime import *

email_sender = "tester.py99@gmail.com"
password = "Li*t0AQGEJ7u("
app_password = "juslsfmekfbyvpnn"

# email_receiver = "boukhedenna.nedjm@gmail.com"
email_receiver = "chihanikarim07@gmail.com"

with SMTP("smtp.gmail.com") as connect:
    connect.starttls()
    connect.login(user=email_sender, password=app_password)
    connect.sendmail(
        from_addr=email_sender,
        to_addrs=email_receiver,
        msg="Subject: SMTP .py Test Email\n\n"
            "This is an automated test Email."
    )
