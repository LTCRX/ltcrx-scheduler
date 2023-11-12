from dataclasses import dataclass
from typing import Optional

from core.services.hashing import Hasher


@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False

    @classmethod
    def create_normal_user(cls, username: str, email: str, password: str):
        return cls(
            id=None,
            username=username,
            email=email,
            hashed_password=Hasher.get_password_hash(password),
        )

    @classmethod
    def create_super_user(cls, username: str, email: str, password: str):
        return cls(
            id=None,
            username=username,
            email=email,
            hashed_password=Hasher.get_password_hash(password),
            is_superuser=True,
        )
