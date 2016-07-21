WTF_CSRF_ENABLED = True
SECRET_KEY = 'thing1'

from app import app
import os

# Email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

#Start Command Line interaction

# administrator list
ADMINS = ['your-gmail-username@gmail.com']
ADMINS = ['chrisja67@gmail.com']


