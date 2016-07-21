# Views: definitions of pages within site

from flask import render_template, flash, redirect, request
from app import app, emails
from config import ADMINS
from .emails import send_email, send_welcome_email
from .forms import LoginForm
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
        print "Email address: " + email_addr
        user = User.query.filter_by(email=email_addr).first()

        if user is None:
            user = User(email=email_addr)
            user.nickname = user.email.split('@')[0]
            db.session.add(user)
            db.session.commit()
            send_welcome_email(user)

            flash('Thankyou for pledging to vote, %s. Email Sent' %
                  (user.nickname))
        else:
            flash('%s, you are already in the database.' %
                  (user.nickname))
        return redirect('/index')
    return render_template('login.html',
	                          title='Sign In',
			                  form=form)
