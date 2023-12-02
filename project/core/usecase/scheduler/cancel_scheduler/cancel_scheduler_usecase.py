from core.domain.scheduler import Scheduler
from core.usecase.usecase_interface import UseCaseInterface
from sqlalchemy.orm import Session
from infrastructure.persistence.repository.postgres_scheduler_repository_adapter import (
    PostgresSchedulerRepositoryAdapter,
)


class CancelSchedulerUseCase(UseCaseInterface):
    def __init__(self, db: Session):
        self.repository = PostgresSchedulerRepositoryAdapter(db)

    def execute(self, scheduler_id: int) -> Scheduler:
        scheduler = self.repository.get_by_id(scheduler_id)
        scheduler.cancel()
        return self.repository.update(scheduler)
