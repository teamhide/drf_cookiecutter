from mongoengine import *


class BaseDocument(Document):
    meta = {
        'abstract': True
    }

    # For type hinting
    @classmethod
    def query(cls, *args, **kwargs) -> QuerySet:
        return cls.objects(*args, **kwargs)


class BaseEmbeddedDocument(EmbeddedDocument):
    meta = {
        'abstract': True
    }
