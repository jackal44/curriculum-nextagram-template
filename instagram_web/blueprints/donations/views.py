from flask import Blueprint, redirect, request, render_template
from instagram_web.util.braintree import *


donations_blueprint = Blueprint('donations',
                                __name__,
                                template_folder='templates')


@donations_blueprint.route("/", methods=["GET"])
def new():
    client_token = gateway.client_token.generate()
    return render_template('donations/new.html', client_token=client_token)
