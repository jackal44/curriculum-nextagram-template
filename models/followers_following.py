from models import base_model
import peewee as pw


class FollowerFollowing (base_model)


fan = pw.ForeignKeyField(User, backref='idol')
idol = pw.ForeignKeyField(User, backref='fan')
approved = pw.BackrefAccessor(default=False)
