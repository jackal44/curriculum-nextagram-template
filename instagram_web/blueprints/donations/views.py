from flask import Blueprint, redirect, request, render_template, flash, url_for
from instagram_web.util.braintree import *
from models.image import Image
from models.donation import Donation
from models.user import User
from flask_login import current_user
from instagram_web.util.sendgrid import send_email

donations_blueprint = Blueprint('donations',
                                __name__,
                                template_folder='templates')

TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]

client_token = gateway.client_token.generate()


@donations_blueprint.route("/<img_id>", methods=["GET"])
def new(img_id):
    # send_email()
    return render_template('donations/new.html', client_token=client_token, img_id=img_id)


@donations_blueprint.route('/complete_donation/<id>', methods=["POST"])
def complete_donation(id):
    amount = request.form['amount']
    payment_method_nonce = request.form['payment_method_nonce']
    image = Image.get_by_id(id)
    user = current_user
    result = transact({
        'amount': amount,
        'payment_method_nonce': payment_method_nonce,
        'options': {
            'submit_for_settlement': True
        }
    })

    if result.is_success or result.transaction:
        donation = Donation(amount=int(amount),
                            image_id=image.id, user_id=user.id, payment_status=True)
        donation.save()
        flash('Donation Successfully created!')
        image_user = User.get_by_id(image.user_id)
        send_email()
        return redirect(url_for('users.show', username_id=image_user.id))
    else:
        for x in result.errors.deep_errors:
            flash('Error: %s: %s' % (x.code, x.message))
        return render_template('donations/new.html', img_id=image.id, client_token=client_token)
