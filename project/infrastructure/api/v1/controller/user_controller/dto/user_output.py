from pydantic import BaseModel, EmailStr

from core.domain.user import User


class UserOutput(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    @classmethod
    def from_domain(cls, user: User) -> "UserOutput":
        return cls(username=user.username, email=user.email, is_active=user.is_active)
