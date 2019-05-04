from flask import Blueprint, render_template, flash, request, redirect, url_for
from models import user


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['get'])
def new():
    return render_template('users/signup.html')


@users_blueprint.route('/signUp', methods=['GET'])
def create():
    s = user.User(username=request.args['username'],
                  email=request.args['email'], password=request.args['password'])

    if s.save():
        flash("Successfully saved")
        return redirect(url_for('users.new'))

    else:
        return render_template('users/welcome.html', username=request.args['username'], email=request.args['email'], password=request.args('password'))


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
