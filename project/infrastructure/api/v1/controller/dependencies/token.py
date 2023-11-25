from typing import Any

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from core.configs.settings import settings
from core.domain.user import User
from core.services.user_services import UserServices
from infrastructure.api.v1.controller.token_controler.exceptions.credentials import (
    credentials_exception,
    credentials_forbidden_exception,
)
from infrastructure.persistence.repository.postgres_user_repository_adapter import (
    PostgresUserRepositoryAdapter,
)
from infrastructure.persistence.repository.session import get_db

oauth2_scheme: Any = OAuth2PasswordBearer(tokenUrl="api/v1/token")


def get_user_by_token(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise credentials_exception
    repository = PostgresUserRepositoryAdapter(db)
    service = UserServices(repository)

    username: str = payload.get("sub")
    user = service.get_user_by_username(username=username)
    if user is None:
        raise credentials_exception
    return user


def get_superuser_by_token(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    user = get_user_by_token(db, token)
    if user.is_superuser:
        return user
    raise credentials_forbidden_exception
