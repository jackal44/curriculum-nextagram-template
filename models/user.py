from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField(unique=False)

    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)

        if duplicate_username:
            self.errors.append('This username has been taken')
