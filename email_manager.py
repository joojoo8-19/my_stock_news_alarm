import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

MY_EMAIL = "hhjc17@naver.com"
NAVER_SERVER = "smtp.naver.com"

class EmailManager:
    def __init__(self):
        load_dotenv()
        self.naver = NAVER_SERVER
        self.my_email = MY_EMAIL
        self.my_password = os.environ.get("MY_EMAIL_PASSWORD")

    def send_email_to_me(self, subject:str, contents:str):
        msg = MIMEText(contents)
        msg["Subject"] = subject
        msg["From"] = self.my_email
        msg["To"] = self.my_email

        with smtplib.SMTP(host=self.naver) as server:
            server.starttls()
            server.login(user=self.my_email, password=self.my_password)
            server.send_message(msg)