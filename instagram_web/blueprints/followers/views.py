from flask import Blueprint


followers_blueprint = Blueprint('followers',
                                __name__,
                                template_folder='templates')


@followers_blueprint.route('/')
def create():
    pass
