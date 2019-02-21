from mongoengine import *
from datetime import datetime


class TimestampMixin:
    created_at = DateTimeField(default=datetime.now().replace(microsecond=0))
    updated_at = DateTimeField(default=datetime.now().replace(microsecond=0))
