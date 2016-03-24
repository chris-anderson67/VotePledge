from flask import render_template, flash, redirect
from app import app, db, emails
from config import ADMINS
# from flask.ext.wtf import Forms
from .emails import send_email, send_welcome_email
from .forms import LoginForm
from .models import User


@app.route('/index')
def index():
    user = {'nickname': 'Chris'}  # placeholder

    return render_template('index.html',
                           title='Home')

# Login / Sign up Page
@app.route('/login', methods=['GET', 'POST'])
@app.route('/')
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data)
            # user.nickname = form.nickname.data
            # if user.nickname is None:
            user.nickname = user.email.split('@')[0]
            db.session.add(user)
            db.session.commit()
            send_welcome_email(user)

            flash('Thankyou for pledging to vote, %s. EMAIL SENT' %
                        (user.nickname))
        else:
            flash('%s, you are already in the database' %
                        (user.nickname))
        return redirect('/index')
    return render_template('login.html',
    			   title='Sign In',
			   form=form)
