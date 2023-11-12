from typing import Optional

from core.services.hashing import Hasher
from core.domain.user import User
from core.ports.user_repository_port import UserRepositoryPort


class UserServices:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def create_new_user(self, user: User) -> User:
        return self.repository.save(user)

    def authenticate_user(self, email: str, password: str):
        user = self.repository.get_user_by_email(email)
        if not user:
            return False
        if not Hasher.verify_password(password, user.hashed_password):
            return False
        return user

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.repository.get_user_by_username(username)
