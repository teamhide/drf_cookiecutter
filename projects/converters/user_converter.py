from typing import NoReturn, Optional, Union
from django.http.request import QueryDict
from rest_framework.request import Request
from rest_framework.utils.serializer_helpers import ReturnDict
from users.models.mongo import User
from users.entities import UserEntity
from auth.entities import AuthEntity
from projects.exceptions import InvalidRequestType


class Converter:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Converter, cls).__new__(cls)
        return cls.instance

    def remove_none_from_dict(self, obj) -> dict:
        return dict(filter(lambda x: x[1], obj.items()))


class UserRepositoryConverter(Converter):
    def user_model_to_entity(self, model: User) -> UserEntity:
        return UserEntity(**model.to_dict())

    def user_entity_to_model(self, entity: UserEntity) -> User:
        return User(**entity.__dict__)


class UserInteractorConverter(Converter):
    def request_to_entity(self, request: Optional[Union[QueryDict, dict]]) -> Union[UserEntity, NoReturn]:
        """Request -> Entity"""
        if type(request) is QueryDict:
            return UserEntity(**request.dict())
        elif type(request) is dict:
            return UserEntity(**request)
        elif type(request) is Request:
            return UserEntity(**request)
        elif type(request) is ReturnDict:
            return UserEntity(**request)
        else:
            raise InvalidRequestType


class AuthRepositoryConverter(Converter):
    pass


class AuthInteractorConverter(Converter):
    def request_to_entity(self, request: Optional[Union[QueryDict, dict]]) -> Union[AuthEntity, NoReturn]:
        """Request -> Entity"""
        if type(request) is QueryDict:
            return AuthEntity(**request.dict())
        elif type(request) is dict:
            return AuthEntity(**request)
        elif type(request) is Request:
            return AuthEntity(**request)
        elif type(request) is ReturnDict:
            return AuthEntity(**request)
        else:
            raise InvalidRequestType
