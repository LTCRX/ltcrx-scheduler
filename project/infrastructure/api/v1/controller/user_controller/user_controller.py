from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from core.services.user_services import UserServices
from infrastructure.api.v1.controller.user_controller.dto.user_create_input import UserCreateInput
from infrastructure.api.v1.controller.user_controller.dto.user_output import UserOutput
from infrastructure.persistence.repository.postgres_user_repository_adapter import (
    PostgresUserRepositoryAdapter,
)
from infrastructure.persistence.repository.session import get_db

router = APIRouter()


@router.post("/", response_model=UserOutput)
def create_user(user_input: UserCreateInput, db: Session = Depends(get_db)) -> UserOutput:
    try:
        repository = PostgresUserRepositoryAdapter(db)
        service = UserServices(repository=repository)

        user = user_input.to_domain()
        user_persisted = service.create_new_user(user)
        return UserOutput.from_domain(user_persisted)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Error: {e}")
