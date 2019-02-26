import abc
from typing import List, Union, NoReturn
from users.models.mongo import User
from users.entities import UserEntity
from projects.exceptions import NotFoundException, AlreadyExistException
from projects.converters import Converter
import mongoengine


class UserRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def _find_user(self, user_id: int) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_id: int) -> UserEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_list(self) -> List[UserEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def save_user(self, entity: UserEntity) -> UserEntity:
        raise NotImplementedError


class UserMongoRepository(UserRepository):
    def __init__(self):
        self.converter = Converter()

    def _find_user(self, user_id: int) -> User:
        """Return User model(private)"""
        return User.objects(user_id=user_id).first()

    def get_user(self, user_id: int) -> Union[UserEntity, NoReturn]:
        """Get a user"""
        user = User.objects(user_id=user_id).first()

        """Return converted User entity or raise Exception"""
        if user:
            return self.converter.model_to_entity(model=user, entity=UserEntity)
        else:
            raise NotFoundException

    def get_user_list(self) -> List[UserEntity]:
        """Get all users"""
        users = User.objects.all()

        """Convert each user to entity"""
        user_entity = []
        for user in users:
            user_entity.append(self.converter.model_to_entity(model=user, entity=UserEntity))
        return user_entity

    def save_user(self, entity: UserEntity) -> UserEntity:
        try:
            """Convert User entity to model"""
            user_model = self.converter.entity_to_model(entity=entity, model=User)

            """Save converted User model"""
            user_model.save()

            """Convert User model to entity and return"""
            return self.converter.model_to_entity(model=user_model, entity=UserEntity)
        except mongoengine.errors.NotUniqueError:
            raise AlreadyExistException
