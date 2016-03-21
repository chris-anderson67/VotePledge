from flask import render_template, flash, redirect
from app import app, db
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')

def index():
    # user = {'nickname': 'Chris'}  # placeholder
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', 
                           title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data)
            user.nickname = user.email.split('@')[0]
            db.session.add(user)
            db.session.commit()

        flash('Login requested for Email="%s", remember_me="%s"' %
              (form.email.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
    			   title='Sign In',
			   form=form)


    			   
