from core.domain.scheduler import Scheduler
from core.usecase.usecase_interface import UseCaseInterface
from sqlalchemy.orm import Session
from infrastructure.persistence.repository.postgres_scheduler_repository_adapter import (
    PostgresSchedulerRepositoryAdapter,
)


class VerifySchedulerByProtocolUseCase(UseCaseInterface):
    def __init__(self, db: Session):
        self.repository = PostgresSchedulerRepositoryAdapter(db)

    def execute(self, protocol: str) -> Scheduler:
        scheduler = self.repository.get_by_protocol(protocol)
        return scheduler
