from datetime import datetime


class UserEntity:
    def __init__(
            self,
            no: int = None,
            user_id: str = None,
            user_pw: str = None,
            created_at: datetime = None,
            updated_at: datetime = None):
        self.no = no
        self.user_id = user_id
        self.user_pw = user_pw
        self.created_at = created_at
        self.updated_at = updated_at
