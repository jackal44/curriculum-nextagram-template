from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from werkzeug.security import generate_password_hash
from models.user import User
from flask_login import login_user


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['get'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/new/create', methods=['POST'])
def create():
    hashed_password = generate_password_hash(request.form['password'])
    s = User(username=request.form['username'],
             email=request.form['email'], password=hashed_password)

    if s.save():
        flash("Successfully saved!")
        login_user(s, force=True)
        return redirect(url_for('sessions.matt_test'))

    else:
        return render_template('users/new.html', username=request.form['username'], email=request.form['email'], password=request.form['password'], errors=s.errors)


@users_blueprint.route('/<username_id>', methods=["GET"])
def show(username_id):

    for person in user.User.select().where(user.User.id == username_id):
        username = person.username
    return render_template('users/individual_user.html', username=username)


@users_blueprint.route('/', methods=["GET"])
def index():
    every_user = []
    for person in user.User:
        every_user.append(person.username)
    return render_template('users/all_users.html', every_user=every_user)


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
