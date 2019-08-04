from models.base_model import BaseModel
import peewee as pw
from playhouse.hybrid import hybrid_property
from config import S3_LOCATION


class User(BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField(unique=False)
    image_path = pw.CharField(unique=False, null=True)
    private = pw.BooleanField(default=False)
    button_status = pw.BooleanField(default=True)

    @hybrid_property
    def is_private(self):
        return True if self.private else False

    @hybrid_property
    def profile_image_url(self):
        return str(S3_LOCATION + self.image_path)

    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_username:
            self.errors.append('This username has been taken')

        elif duplicate_email:
            self.errors.append('This email has been used')

    def is_authenticated():
        return True

    def is_active():
        return True
