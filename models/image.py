from models.base_model import BaseModel
import peewee as pw


class Image(BaseModel):
    img = pw.CharField(unique=False)

    # def is_authenticated():
    #     return True

    # def is_active():
    #     return True
