WTF_CSRF_ENABLED = True
SECRET_KEY = 'thing1'


import os
basedir = os.path.abspath(os.path.dirname(__file__))

# email support
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT   = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

ADMINS = ['chrisja67@gmail.com']

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
