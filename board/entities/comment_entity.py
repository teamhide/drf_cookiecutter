from datetime import datetime


class CommentEntity:
    def __init__(self,
                 article_id: int = None,
                 user_id: str = None,
                 body: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None):
        self.article_id = article_id
        self.user_id = user_id
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at
