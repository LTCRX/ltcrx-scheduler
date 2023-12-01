from typing import List

from core.domain.scheduler import Scheduler
from core.usecase.usecase_interface import UseCaseInterface
from sqlalchemy.orm import Session
from infrastructure.persistence.repository.postgres_scheduler_repository_adapter import (
    PostgresSchedulerRepositoryAdapter,
)


class GetAllSchedulerUseCase(UseCaseInterface):
    def __init__(self, db: Session):
        self.repository = PostgresSchedulerRepositoryAdapter(db)

    def execute(self, user_id: int) -> List[Scheduler]:
        return self.repository.get_all_by_user(user_id)
