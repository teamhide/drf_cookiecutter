from users.repositories import UserRepository, UserMongoRepository
from board.repositories import BoardRepository, BoardMongoRepository


class RepositoryServiceProvider:
    def inject(self, binder):
        binder.bind_to_provider(UserRepository, UserMongoRepository)
        binder.bind_to_provider(BoardRepository, BoardMongoRepository)
