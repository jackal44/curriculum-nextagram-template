from models.base_model import BaseModel
import peewee as pw
from models.user import User
from models.image import Image


class FollowerFollowing (BaseModel):
    fan = pw.ForeignKeyField(User, backref='idol')
    idol = pw.ForeignKeyField(User, backref='fan')
    approved = pw.BooleanField(default=False)
