from flask import Blueprint, render_template, flash, request, redirect, url_for
from werkzeug.security import generate_password_hash
from models import user


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['get'])
def new():
    return render_template('users/sign_up.html')


@users_blueprint.route('/sign_up', methods=['GET'])
def create():
    hashed_password = generate_password_hash(request.args['password'])
    s = user.User(username=request.args['username'],
                  email=request.args['email'], password=hashed_password)

    if s.save():
        flash("Successfully saved")
        return redirect(url_for('users.new'))

    else:
        return render_template('users/sign_up.html', username=request.args['username'], email=request.args['email'], password=request.args['password'], errors=s.errors)


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
