import inject
from typing import List
from users.entities import UserEntity
from users.repositories import UserRepository
from projects.converters import UserInteractorConverter


class UserInteractor:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository
        self.converter = UserInteractorConverter()


class CreateUserInteractor(UserInteractor):
    def execute(self, request: dict) -> UserEntity:
        user_entity = self.converter.request_to_entity(request=request)
        return self.repository.save_user(entity=user_entity)


class GetUserInteractor(UserInteractor):
    def execute(self, no: int) -> UserEntity:
        return self.repository.get_user(user_id=no)


class UserListInteractor(UserInteractor):
    def execute(self) -> List[UserEntity]:
        return self.repository.get_user_list()
