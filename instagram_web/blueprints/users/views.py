from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from werkzeug.security import generate_password_hash
from models.user import User
from flask_login import login_user, current_user


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
        return redirect(url_for('users.show', username_id=current_user.id))

    else:
        return render_template('users/new.html', username=request.form['username'], email=request.form['email'], password=request.form['password'], errors=s.errors)


@users_blueprint.route('/image', methods=["GET"])
def view():
    return render_template('upload_image.html')


@users_blueprint.route('/<username_id>', methods=["GET"])
def show(username_id):
    return render_template('users/user_page.html')

    # for person in User.select().where(User.id == username_id):
    #     username = person.username
    # return render_template('users/individual_user.html', username=username)


@users_blueprint.route('/', methods=["GET"])
def index():
    pass
    # every_user = []
    # for person in User:
    #     every_user.append(person.username)
    # return render_template('users/all_users.html', every_user=every_user)


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    if current_user.is_authenticated:
        return render_template('users/edit.html')

    else:
        flash("user not logged in, invalid request")
        return redirect(url_for('home'))


@users_blueprint.route('/edit_image', methods=['GET'])
def edit_profile_pic():
    return render_template('users/image_form.html')


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    s = User.update(
        username=request.form['username'], email=request.form['email']).where(User.id == id)
    s.execute()
    flash('username has been updated')
    return redirect(url_for('users.show', username_id=current_user.id))
