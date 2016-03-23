WTF_CSRF_ENABLED = True
SECRET_KEY = 'thing1'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
ADMINS = ['chrisja67@gmail.com']

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

