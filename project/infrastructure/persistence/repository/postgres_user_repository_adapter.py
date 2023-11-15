from typing import Optional

from core.domain.user import User
from core.ports.user_repository_port import UserRepositoryPort
from infrastructure.persistence.models.users import UserModel
from sqlalchemy.orm import Session


class PostgresUserRepositoryAdapter(UserRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def save(self, user: User) -> User:
        user_model = UserModel.from_domain(user)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model.to_domain()

    def get_user_by_email(self, email: str) -> Optional[User]:
        user_model = self.db.query(UserModel).filter(UserModel.email == email).first()
        if user_model is None:
            return None
        return user_model.to_domain()

    def get_user_by_username(self, username: str) -> Optional[User]:
        user_model = self.db.query(UserModel).filter(UserModel.username == username).first()
        if user_model is None:
            return None
        return user_model.to_domain()
