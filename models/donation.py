from models.base_model import BaseModel
from models.user import User
from models.image import Image
import peewee as pw


class Donation(BaseModel):
    user = pw.ForeignKeyField(User, null=True)
    image = pw.ForeignKeyField(Image, null=True)
    amount = pw.DecimalField(null=False, default=0.00, decimal_places=2)
    payment_status = pw.BooleanField(null=False, default=False)
