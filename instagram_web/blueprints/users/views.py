from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from werkzeug.security import generate_password_hash
from models.user import User
from models.image import Image
from models.followers_following import FollowerFollowing
from flask_login import login_user, current_user
from werkzeug.utils import secure_filename


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['get'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/new/create', methods=['POST'])
def create_user():
    hashed_password = generate_password_hash(request.form['password'])
    s = User(username=request.form['username'],
             email=request.form['email'], password=hashed_password, image_path="default-user.png")

    if s.save():
        flash("Successfully saved!")
        login_user(s, force=True)
        return redirect(url_for('users.show', username_id=current_user.id))

    else:
        return render_template('users/new.html', username=request.form['username'], email=request.form['email'], password=request.form['password'], errors=s.errors)


@users_blueprint.route('/<username_id>', methods=["GET"])
def show(username_id):
    user_img = Image.select().where(Image.user_id == username_id)
    user = User.get_by_id(username_id)

    followers = FollowerFollowing.select().where(FollowerFollowing.fan ==
                                                 current_user.id and FollowerFollowing.idol == username_id)

    if followers:
        FollowerFollowing.update(button=False).where(
            FollowerFollowing.fan == current_user.id and FollowerFollowing == username_id)
    return render_template('users/user_profile.html', user_img=user_img, user=user, followers=followers)


@users_blueprint.route('/home/<username_id>', methods=["GET"])
def show_home(username_id):
    user = User.select().where(User.username != current_user.username)
    return render_template('users/home.html', User=user)


@users_blueprint.route('/image', methods=["GET"])
def view():
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    pass


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    if current_user.is_authenticated:
        return render_template('users/edit_details.html')

    else:
        flash("user not logged in, invalid request")
        return redirect(url_for('home'))


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    s = User.update(
        username=request.form['username'], email=request.form['email']).where(User.id == id)
    s.execute()
    flash('username has been updated')
    return redirect(url_for('users.show', username_id=current_user.id))
