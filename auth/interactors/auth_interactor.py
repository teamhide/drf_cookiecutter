import inject
from typing import List
from rest_framework.utils.serializer_helpers import ReturnDict
from auth.entities import AuthEntity
from users.repositories import UserRepository
from projects.converters import AuthInteractorConverter


class AuthInteractor:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository
        self.converter = AuthInteractorConverter()


class CreateTokenInteractor(AuthInteractor):
    def execute(self, request: ReturnDict):
        auth_entity = self.converter.request_to_entity(request=request)
        print(auth_entity.__dict__)
        return
        user = self.repository.get_user()
