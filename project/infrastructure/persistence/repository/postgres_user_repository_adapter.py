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
