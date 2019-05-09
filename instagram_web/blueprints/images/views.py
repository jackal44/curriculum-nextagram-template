from flask import Blueprint, redirect, render_template, url_for
from instagram_web.util.helpers import *
from config import S3_BUCKET
from flask_login import current_user
from werkzeug.utils import secure_filename
from models.user import User
from models.image import Image

images_blueprint = Blueprint('images',
                             __name__,
                             template_folder='templates')


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@images_blueprint.route("/upload", methods=["POST"])
def upload_profile_pic():
    if "user_file" not in request.files:
        flash("No user_file key in request.files")
        return redirect(url_for('images.edit_profile_pic'))

    file = request.files["user_file"]

    if file.filename == "":
        return "Please select a file"

    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        image_url = upload_file_to_s3(file, S3_BUCKET)
        update = User.update(profile_pic=image_url).where(
            User.id == current_user.id)
        update.execute()
        return redirect(url_for('users.show', username_id=current_user.id))


@images_blueprint.route('/upload_image', methods=['post'])
def create_upload_pic():

    if "user_file" not in request.files:
        flash("No user_file key in request.files")
        return redirect(url_for('users.edit_profile_pic'))

    file = request.files["user_file"]

    if file.filename == "":
        return "Please select a file"

    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        image_url = upload_file_to_s3(file, S3_BUCKET)
        image = Image.create(img=image_url, user_id=current_user.id)
        image.save()
        return redirect(url_for('users.show', username_id=current_user.id))


@images_blueprint.route('/edit_image', methods=['GET'])
def edit_upload_pic():
    return render_template('users/edit_upload_pic.html')


@images_blueprint.route('/edit_profile_image', methods=['GET'])
def edit_profile_pic():
    return render_template('users/edit_profile.html')
