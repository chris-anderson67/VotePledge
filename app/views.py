# Views: definitions of pages within site
from flask import render_template, flash, redirect, request
from app import app, emails
from config import ADMINS
from .emails import send_email, send_welcome_email
from .forms import LoginForm
import db_manip
# from .models import User


# Homepage: not sure what to put here yet
@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Chris'}  # placeholder
    return render_template('index.html',
                           title='Home')

# Login / Sign up Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        email_addr = form.email.data
        nickname = email_addr.split('@')[0]
        print "Email address: " + email_addr
        db = db_manip.get_db(app)
        cur = db.cursor()
        cur.execute("SELECT rowid FROM users WHERE email = ?", (email_addr,))
        data = cur.fetchone()

        if data is None:
            db.execute('insert into users (email) values (?)', (email_addr,))
            db.commit()

            send_welcome_email(email_addr)
            flash('Thankyou for pledging to vote, %s. Email Sent' %
                  (nickname))

        else:
            flash('%s, you are already in the database.' %
                  (nickname))
        return redirect('/index')

    return render_template('login.html',
	                   title='Sign In',
			   form=form)
