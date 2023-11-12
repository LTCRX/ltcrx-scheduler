from pydantic import BaseModel, EmailStr

from core.domain.user import User


class UserCreateInput(BaseModel):
    username: str
    email: EmailStr
    password: str

    def to_domain(self) -> User:
        return User.create_normal_user(
            username=self.username, email=self.email, password=self.password
        )
