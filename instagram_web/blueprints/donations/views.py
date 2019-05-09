from flask import Blueprint


donations_blueprint = Blueprint('donations',
                                __name__,
                                template_folder='templates')
