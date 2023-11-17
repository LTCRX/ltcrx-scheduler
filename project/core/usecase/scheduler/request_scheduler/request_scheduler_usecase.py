from core.usecase.scheduler.request_scheduler.dto import (
    RequestSchedulerInput,
    RequestSchedulerOutput,
)
from core.usecase.usecase_interface import UseCaseInterface
from sqlalchemy.orm import Session

from infrastructure.persistence.repository.postgres_scheduler_repository_adapter import (
    PostgresSchedulerRepositoryAdapter,
)


class RequestSchedulerUseCase(UseCaseInterface):
    def __init__(self, db: Session):
        self.repository = PostgresSchedulerRepositoryAdapter(db)

    def execute(self, command_input: RequestSchedulerInput) -> RequestSchedulerOutput:
        scheduler = command_input.to_domain()
        scheduler_persisted = self.repository.save(scheduler)
        return RequestSchedulerOutput(protocol=scheduler_persisted.protocol)
