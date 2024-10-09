from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash
from .models import User
from . import db

# create a blueprint
authbp = Blueprint('auth', __name__ )

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user = db.session.scalar(db.select(User).where(User.name==user_name))

        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user.password_hash, password): 
            error = 'Incorrect password'
        if error is None:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=form, heading='Login')

@authbp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
            uname = form.username.data
            pwd = form.password.data
            email = form.email.data
            user = db.session.scalar(db.select(User).where(User.name==uname))

            if user:
                flash('Username already exists, please try another')
                return redirect(url_for('auth.register'))

            pwd_hash = generate_password_hash(pwd)

            new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('main.index'))
    else:
        return render_template('user.html', form=form, heading='Register')
    
@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))