from models.base_model import BaseModel
import peewee as pw
from models.user import User
from models.image import Image
from playhouse.hybrid import hybrid_property


class FollowerFollowing (BaseModel):
    fan = pw.ForeignKeyField(User, backref='idol')
    idol = pw.ForeignKeyField(User, backref='fan')
    approved = pw.BooleanField(default=False)
    button = pw.BooleanField(default=True)

    @hybrid_property
    def is_approve():
        return True if approved else False
