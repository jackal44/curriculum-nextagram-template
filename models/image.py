from models.base_model import BaseModel
from models.user import User
import peewee as pw
from config import S3_LOCATION
from playhouse.hybrid import hybrid_property


class Image(BaseModel):
    image_path = pw.CharField(unique=False)
    user = pw.ForeignKeyField(User, backref='images')

    @hybrid_property
    def image_url(self):
        return str(S3_LOCATION + self.image_path)

    def is_authenticated():
        return True

    def is_active():
        return True
