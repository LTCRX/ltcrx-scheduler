from dataclasses import asdict
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean

from core.domain.user import User
from infrastructure.persistence.models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    course_level = Column(String, nullable=True)
    cpf = Column(String, nullable=True)
    rg = Column(String, nullable=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    project_title = Column(String, nullable=True)
    project_description = Column(String, nullable=True)
    supervisor = Column(String, nullable=True)
    department = Column(String, nullable=True)

    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    schedulers = relationship("SchedulerModel", back_populates="user")

    def to_domain(self) -> User:
        return User(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            is_superuser=self.is_superuser,
            firstname=self.firstname,
            course_level=self.course_level,
            cpf=self.cpf,
            rg=self.rg,
            address=self.address,
            phone=self.phone,
            project_title=self.project_title,
            project_description=self.project_description,
            supervisor=self.supervisor,
            department=self.department,
        )

    @classmethod
    def from_domain(cls, user: User) -> "UserModel":
        return cls(**asdict(user))
