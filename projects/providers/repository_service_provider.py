from users.repositories import UserRepository, UserMongoRepository
from board.repositories import BoardRepository, BoardMongoRepository


class RepositoryServiceProvider:
    @staticmethod
    def inject(binder):
        binder.bind_to_provider(UserRepository, UserMongoRepository)
        binder.bind_to_provider(BoardRepository, BoardMongoRepository)
