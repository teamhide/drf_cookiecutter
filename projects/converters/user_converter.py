from users.models.mongo import User
from users.entities import UserEntity
from projects.converters import Converter


class UserInteractorConverter(Converter):
    def user_dto_to_entity(self, dto) -> UserEntity:
        return UserEntity(**dto.__dict__)


class UserRepositoryConverter(Converter):
    def user_model_to_entity(self, model: User) -> UserEntity:
        user_entity = self._model_to_entity(model=model, entity=UserEntity)
        return user_entity

    def user_entity_to_model(self, entity: UserEntity) -> User:
        return self._entity_to_model(entity=entity, model=User)
