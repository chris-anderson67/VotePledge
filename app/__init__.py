from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager

lm = LoginManager()
lm.init_app(app)

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
