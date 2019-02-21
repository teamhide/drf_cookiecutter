from projects.providers.repository_service_provider import RepositoryServiceProvider


class AppServiceProvider:
    def __init__(self):
        self.repository_provider = RepositoryServiceProvider()

    def inject(self, binder):
        self.repository_provider.inject(binder)
