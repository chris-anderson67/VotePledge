from flask import Flask

import os
import sqlite3
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
import logging
import sys

app = Flask(__name__)
app.config.from_object('config')
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'votepledge.db'),
    SECRET_KEY='dev_key'
))
mail = Mail(app)
# bootstrap = Bootstrap(app)

 

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


from app import views
