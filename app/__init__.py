from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
import logging

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)
bootstrap = Bootstrap(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


from app import views, models
