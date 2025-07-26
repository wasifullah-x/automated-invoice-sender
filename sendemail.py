import os
from pathlib import Path
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from dotenv import load_dotenv

EMAIL_SERVER = "smtp.gmail.com"
PORT = 587

parent_directory = Path(__file__).resolve().parent
envfile = parent_directory / ".env"
load_dotenv(envfile)

sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")

def send_email(subject, reciever_mail, name, service, invoice_no, amount, due_date, attachment_path = None):

    msg = EmailMessage()
    msg["subject"] = subject
    msg["From"] = formataddr(("Wasif", sender_email))
    msg["To"] = reciever_mail
    msg["BCC"] = sender_email

    msg.set_content(
        f"""
            Hi {name}, I'm writing this mail to tell you that your payment with {invoice_no} for {service} work
            due date has passed which was today {due_date}. I request you to pay the amount which is ${amount} 
            as soon as possible.
            Regards 
            Wasif
        """
    )

    if attachment_path:
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = Path(attachment_path).name
            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, reciever_mail, msg.as_string())



