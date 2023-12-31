from abc import ABC, abstractmethod

from core.domain.user import User


class UserRepositoryPort(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        pass
