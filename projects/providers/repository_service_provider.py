from users.repositories import UserRepository, UserMongoRepository


class RepositoryServiceProvider:
    def inject(self, binder):
        binder.bind_to_provider(UserRepository, UserMongoRepository)
