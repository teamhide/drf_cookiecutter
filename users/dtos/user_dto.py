from dataclasses import dataclass


@dataclass
class CreateUserDto:
    user_id: str = None
    user_pw: str = None
