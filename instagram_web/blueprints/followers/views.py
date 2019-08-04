from flask import Blueprint, redirect, url_for, flash
from models.user import User
from models.followers_following import FollowerFollowing
from flask_login import current_user


followers_blueprint = Blueprint('followers',
                                __name__,
                                template_folder='templates')


@followers_blueprint.route('/<username>')
def create(username):
    user = User.get_or_none(User.username == username)
    s = FollowerFollowing.create(
        fan_id=current_user.id, idol_id=user.id)

    if not user.is_private and s.save():
        flash("You have successfully followed {}!".format(username))
        return redirect(url_for('users.show', username_id=user.id))
