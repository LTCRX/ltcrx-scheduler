from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.exceptions.scheduler_exceptions import SchedulerNotFoundError

from core.domain.user import User
from core.usecase.scheduler.approve_scheduler.approve_scheduler_usecase import (
    ApproveSchedulerUseCase,
)
from core.usecase.scheduler.approve_scheduler.dto import ApproveSchedulerOutput
from core.usecase.scheduler.get_all_scheduler.dto import GetAllSchedulerOutput, FiltersInput
from core.usecase.scheduler.get_all_scheduler_by_user.dto import GetAllSchedulerByUserOutput
from core.usecase.scheduler.get_all_scheduler.get_all_scheduler_usecase import (
    GetAllSchedulerUseCase,
)
from core.usecase.scheduler.reject_scheduler.dto import RejectSchedulerOutput
from core.usecase.scheduler.reject_scheduler.reject_scheduler_usecase import RejectSchedulerUseCase
from core.usecase.scheduler.verify_scheduler_by_protocol.dto import VerifyByProtocolOutput
from core.usecase.scheduler.request_scheduler.dto import (
    RequestSchedulerInput,
    RequestSchedulerOutput,
)
from core.usecase.scheduler.request_scheduler.request_scheduler_usecase import (
    RequestSchedulerUseCase,
)
from core.usecase.scheduler.verify_scheduler_by_protocol.verify_scheduler_by_protocol_usecase import (
    VerifySchedulerByProtocolUseCase,
)
from infrastructure.api.v1.controller.dependencies.token import (
    get_user_by_token,
    get_superuser_by_token,
)
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


@router.get("/{protocol}/verify-status", response_model=VerifyByProtocolOutput)
def verify_status(protocol: str, db: Session = Depends(get_db)) -> VerifyByProtocolOutput:
    try:
        usecase = VerifySchedulerByProtocolUseCase(db)
        scheduler = usecase.execute(protocol)
        return VerifyByProtocolOutput.from_domain(scheduler)
    except SchedulerNotFoundError as s:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(s))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/{scheduler_id}/approve", response_model=ApproveSchedulerOutput)
def approve_scheduler(
    scheduler_id: int,
    current_user: User = Depends(get_superuser_by_token),
    db: Session = Depends(get_db),
):
    usecase = ApproveSchedulerUseCase(db)

    try:
        scheduler = usecase.execute(scheduler_id)
        return ApproveSchedulerOutput.from_domain(scheduler)
    except SchedulerNotFoundError as s:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(s))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/{scheduler_id}/reject", response_model=RejectSchedulerOutput)
def reject_scheduler(
    scheduler_id: int,
    current_user: User = Depends(get_superuser_by_token),
    db: Session = Depends(get_db),
):
    usecase = RejectSchedulerUseCase(db)

    try:
        scheduler = usecase.execute(scheduler_id)
        return RejectSchedulerOutput.from_domain(scheduler)
    except SchedulerNotFoundError as s:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(s))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/all", response_model=List[GetAllSchedulerOutput])
def get_all_scheduler(
    filters: FiltersInput = Depends(),
    current_superuser: User = Depends(get_superuser_by_token),
    db: Session = Depends(get_db),
):
    usecase = GetAllSchedulerUseCase(db)

    try:
        schedulers = usecase.execute(filters)
        return GetAllSchedulerOutput.from_domain(schedulers)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/{current_user}/all", response_model=List[GetAllSchedulerByUserOutput])
def get_all_scheduler_by_user(
    current_user: User = Depends(get_user_by_token),
    db: Session = Depends(get_db),
):
    usecase = GetAllSchedulerUseCase(db)

    try:
        schedulers = usecase.execute(current_user.id)
        return GetAllSchedulerByUserOutput.from_domain(schedulers)
    except SchedulerNotFoundError as s:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(s))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
