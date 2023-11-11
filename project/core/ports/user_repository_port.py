from abc import ABC, abstractmethod

from core.domain.user import User


class UserRepositoryPort(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass