from datetime import datetime
from mongoengine import *
from projects.models import BaseDocument


class User(BaseDocument):
    no = SequenceField()
    user_id = StringField(required=True)
    user_pw = StringField(required=True)
    created_at = DateTimeField(default=datetime.now().replace(microsecond=0))
    updated_at = DateTimeField(default=datetime.now().replace(microsecond=0))
