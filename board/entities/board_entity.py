from datetime import datetime
from typing import List


class ArticleEntity:
    def __init__(self,
                 article_id: int = None,
                 user_id: str = None,
                 subject: str = None,
                 body: str = None,
                 comments: List = None,
                 password: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None):
        self.article_id = article_id
        self.user_id = user_id
        self.subject = subject
        self.body = body
        self.comments = comments
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at


class CommentEntity:
    def __init__(self,
                 user_id: str = None,
                 body: str = None):
        self.user_id = user_id
        self.body = body
