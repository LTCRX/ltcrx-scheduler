from infrastructure.persistence.repository.postgres_scheduler_repository_adapter import (
    PostgresSchedulerRepositoryAdapter,
)

class VerifySchedulerByProtocolUseCase(UseCaseInterface):
    def __init__(self, db: Session):
        self.repository = PostgresSchedulerRepositoryAdapter(db)

    def execute(self, protocol: str):
        scheduler = self.repository.get_by_protocol(protocol)
        if scheduler is None:
            return 'error'
        else:
            return scheduler
