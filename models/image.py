from models.base_model import BaseModel
from models.user import User
import peewee as pw


class Image(BaseModel):
    img = pw.CharField(unique=False)
    user = pw.ForeignKeyField(User, backref='images', null=False)

    # def is_authenticated():
    #     return True

    # def is_active():
    #     return True
