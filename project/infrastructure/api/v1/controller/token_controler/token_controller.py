from datetime import timedelta

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.configs.settings import settings
from core.services.security import create_access_token
from core.services.user_services import UserServices
from infrastructure.api.v1.controller.token_controler.dto.token_output import TokenOutput
from infrastructure.persistence.repository.postgres_user_repository_adapter import (
    PostgresUserRepositoryAdapter,
)
from infrastructure.persistence.repository.session import get_db

router = APIRouter()


@router.post("/", response_model=TokenOutput)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> TokenOutput:
    """
    Generate a token to access endpoints
    """
    repository = PostgresUserRepositoryAdapter(db)
    service = UserServices(repository=repository)

    user = service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return TokenOutput(access_token=access_token, token_type="bearer")
