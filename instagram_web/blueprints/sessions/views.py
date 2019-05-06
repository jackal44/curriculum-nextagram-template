from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from models.user import User
from app import login_manager
from flask_login import login_user


sessions_blueprint = Blueprint('sessions',
                               __name__,
                               template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


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
        login_user(user, force=True)
        return render_template('try.html')
