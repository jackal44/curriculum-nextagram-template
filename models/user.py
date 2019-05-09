from models.base_model import BaseModel
import peewee as pw
from playhouse.hybrid import hybrid_property


class User(BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField(unique=False)
    profile_pic = pw.CharField(
        unique=False, null=True)

    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_username:
            self.errors.append('This username has been taken')

        elif duplicate_email:
            self.errors.append('This email has been used')

    def is_authenticated():
        return True

    @hybrid_property
    def profile_image_url(self):
        return AWS_S3_DOMAIN + self.image_path

    def is_active():
        return True
