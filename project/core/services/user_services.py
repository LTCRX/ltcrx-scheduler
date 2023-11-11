from core.domain.user import User
from core.ports.user_repository_port import UserRepositoryPort


class UserServices:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def create_new_user(self, user: User) -> User:
        return self.repository.save(user)
