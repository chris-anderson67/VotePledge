from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)
bootstrap = Bootstrap(app)


from app import views, models
