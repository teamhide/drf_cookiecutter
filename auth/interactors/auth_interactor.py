import inject
from rest_framework.utils.serializer_helpers import ReturnDict
from users.repositories import UserRepository
from projects.converters import Converter


class AuthInteractor:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository
        self.converter = Converter()


class CreateTokenInteractor(AuthInteractor):
    def execute(self, request: ReturnDict):
        pass
