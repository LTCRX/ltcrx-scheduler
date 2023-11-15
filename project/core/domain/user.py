from dataclasses import dataclass
from typing import Optional

from core.services.hashing import Hasher


@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    hashed_password: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False
    firstname: Optional[str] = None
    course_level: Optional[str] = None
    cpf: Optional[str] = None
    rg: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    project_title: Optional[str] = None
    project_description: Optional[str] = None
    supervisor: Optional[str] = None
    department: Optional[str] = None

    @classmethod
    def create_normal_user(cls, username: str, email: str, password: str, **kwargs) -> "User":
        return cls(
            id=None,
            username=username,
            email=email,
            hashed_password=Hasher.get_password_hash(password),
            **kwargs
        )

    @classmethod
    def create_super_user(cls, username: str, email: str, password: str, **kwargs) -> "User":
        return cls(
            username=username,
            email=email,
            hashed_password=Hasher.get_password_hash(password),
            is_superuser=True,
            **kwargs
        )
