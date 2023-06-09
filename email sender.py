from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'youremailaddress@gmail.com'
email_passwoed = 'password'

email_reciver = 'reciver@gmail.com'
subject = "This is a test run"
body = """
This is a Project
"""
em = EmailMessage()
em['From'] = email_sender
em['TO'] = email_reciver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_passwoed)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
