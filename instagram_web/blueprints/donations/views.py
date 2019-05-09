from flask import Blueprint, redirect, request, render_template
from instagram_web.util.braintree import *


donations_blueprint = Blueprint('donations',
                                __name__,
                                template_folder='templates')


client_token = gateway.client_token.generate({
    "customer_id": a_customer_id
})


@donations_blueprint.route("/", methods=["GET"])
def new():
    return render_template('donations/new.html')


@donations_blueprint.route("/client_token", methods=["GET"])
def client_token():
    return gateway.client_token.generate()
