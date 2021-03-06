from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from models.user import User
from flask_login import login_user, logout_user, current_user


sessions_blueprint = Blueprint('sessions',
                               __name__,
                               template_folder='templates')


@sessions_blueprint.route("/logout")
def destroy():
    logout_user()
    flash('User has been successfully logged out')
    return redirect(url_for('users.new'))


@sessions_blueprint.route('/new', methods=['get'])
def new():
    return render_template('new.html')


@sessions_blueprint.route('/try/test', methods=['GET'])
def matt_test():
    return render_template('try.html')


@sessions_blueprint.route('/try', methods=['POST'])
def create():
    password = request.form['password']
    user = User.get_or_none(User.email == request.form['email'])

    if not user:
        flash('Incorrect email provided')
        return redirect(url_for('sessions.new'))

    if not check_password_hash(user.password, password):
        flash('Incorrect password')
        return redirect(url_for('sessions.new'))

    else:
        flash("You have successfully logged in")
        # login
        login_user(user, remember=True)
        return redirect(url_for('users.show', username_id=current_user.id))
