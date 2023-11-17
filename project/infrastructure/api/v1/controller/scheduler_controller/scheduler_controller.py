from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.domain.user import User
from core.usecase.scheduler.request_scheduler.dto import (
    RequestSchedulerInput,
    RequestSchedulerOutput,
)
from core.usecase.scheduler.request_scheduler.request_scheduler_usecase import (
    RequestSchedulerUseCase,
)
from infrastructure.api.v1.controller.dependencies.token import get_user_by_token
from infrastructure.persistence.repository.session import get_db

router = APIRouter()


@router.post("/request-scheduler", response_model=RequestSchedulerOutput)
def request_scheduler(
    scheduler_input: RequestSchedulerInput,
    current_user: User = Depends(get_user_by_token),
    db: Session = Depends(get_db),
) -> RequestSchedulerOutput:
    scheduler_input.set_user(current_user)
    usecase = RequestSchedulerUseCase(db)
    return usecase.execute(scheduler_input)
