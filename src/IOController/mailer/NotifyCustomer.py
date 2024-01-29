import smtplib
import json

'''
This file handles sending emails.
As is, it's just a general purpose emailing function,
however the IOController can leverage it to send notifications
to Mocktender users when the liquid level of a liquid in the system
is low.

Author: Ethan Bradley, 101158848
'''

def __send(data: dict, content: str, subject: str, recipient: str):
    '''
    Starts a session with googles smtp server and 
    sends an email using the provided information parameters

    content: The body of the email to send to the user
    subject: the subject line of the email
    recipient: the email address of the user
    '''
    PORT = 587
    SERVER = "smtp.gmail.com"
    PASSWORD: str = data["app_pw"]
    
    SENDER_EMAIL: str = data["sender"]
    SENDER_NAME: str = data["sender_name"]
    RECIPIENT_EMAIL = recipient
    RECIPIENT_NAME = RECIPIENT_EMAIL.split("@").pop(0)

    # start smtp session
    session = smtplib.SMTP(SERVER, PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(SENDER_EMAIL, PASSWORD)

    # prepare message for sending
    message = f"from: {SENDER_NAME} <{SENDER_EMAIL}>\r\n"
    message += f"to: {RECIPIENT_NAME} <{RECIPIENT_EMAIL}>\r\n"
    message += f"subject: {subject}\r\n\r\n"
    message += content

    # send email and return
    session.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message)
    session.quit


def send(content, subject, recipient="no-reply@gmail.com"):
    '''
    Emails the Mocktender user with the supplied message
    and subject.
    '''
    with open("mailer/notif_config.json", 'r') as j:
        data =  dict(json.loads(j.read()))
        data.update({"recipient": recipient})
        
        try:
            __send(data, content, subject, recipient)
            print("Email sent successfully")
        except:
            print("Something went wrong and the email could not be sent")
