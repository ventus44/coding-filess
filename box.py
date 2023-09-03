#we first import the email message lib
from email.message import EmailMessage
#the we import the ssl lib 
import ssl
#and then smtplib
import smtplib
#we make a vairble and we store our email sender inside
email_sender = "thanoskats7@gmail.com"
#we make anotherone for our password
email_password = "reopyrwgansdslig"
#we make one for our reciever 
email_receiver = "voula1959@hotmail.com"
#this is the subject of the email
Subject = "eyyyy"
#this is the body of the email
Body = '''
ekana to sxedio
'''
#here we store in variables the messge, sender and receiver functions
em = EmailMessage()
em["from"] = email_sender
em["To"] = email_receiver
em["subject"] = Subject
em.set_content(Body)
#here we print out the context of the email to make it secure
context = ssl.create_default_context()
#here we use our libraries to give the okay to the email to be sent
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
