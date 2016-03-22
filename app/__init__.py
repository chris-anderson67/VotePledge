from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)


from app import views, models
