from flask import Flask, request, session, g
import os
import sqlite3
from flask_cli import FlaskCLI
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
import logging
import sys
import db_manip

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config.from_object('config')
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'votepledge.db'),
    SECRET_KEY='dev_key'
))
FlaskCLI(app)
mail = Mail(app)
# bootstrap = Bootstrap(app)


@app.teardown_appcontext
def close_db_teardown(error):
    db_manip.close_db(error)

@app.cli.command('init_db')
def initdb_command():
    db_manip.init_db(app)
    print 'INITIALIZED_DATABASE'
# Conects to specific db

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


from app import views
