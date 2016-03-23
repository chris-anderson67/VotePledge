from flask.ext.mail import Message
from flask import render_template
from config import ADMINS
from app import app, mail
from .decorators import async

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_welcome_email(user):
    send_email('You Pledged your Vote: Thank you!',
               ADMINS[0], [user.email],
               render_template("new_user_email.txt",
                               user=user),
               render_template("new_user_email.html",
                               user=user))
               
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)
    return True
