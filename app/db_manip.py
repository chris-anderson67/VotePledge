import sqlite3
from flask import Flask, g


def connect_db(app):
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Opens new database connection
def get_db(app):
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db(app)
    return g.sqlite_db

# Close db on app exit
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# Makes db with schema.sql file
def init_db(app):
    db = get_db(app)
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Command: 'flask init_db'

