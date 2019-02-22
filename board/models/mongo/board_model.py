from datetime import datetime
from mongoengine import *
from projects.models import BaseDocument, BaseEmbeddedDocument
from users.models.mongo import User


class Comment(BaseEmbeddedDocument):
    comment_id = SequenceField()
    user_id = ReferenceField(User)
    body = StringField()
    created_at = DateTimeField(default=datetime.now().replace(microsecond=0))
    updated_at = DateTimeField(default=datetime.now().replace(microsecond=0))


class Article(BaseDocument):
    article_id = SequenceField()
    user_id = ReferenceField(User, reverse_delete_rule=CASCADE)
    subject = StringField()
    body = StringField()
    comments = ListField(EmbeddedDocumentField(Comment), required=False)
    password = StringField()
    created_at = DateTimeField(default=datetime.now().replace(microsecond=0))
    updated_at = DateTimeField(default=datetime.now().replace(microsecond=0))
