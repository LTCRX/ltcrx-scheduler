from sqlalchemy.orm import Session

from core.domain.scheduler import Scheduler
from core.exceptions.scheduler_exceptions import SchedulerNotFoundError
from core.ports.scheduler_repository_port import SchedulerRepositoryPort
from infrastructure.persistence.models.schedulers import SchedulerModel


class PostgresSchedulerRepositoryAdapter(SchedulerRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def save(self, scheduler: Scheduler) -> Scheduler:
        scheduler_model = SchedulerModel.from_domain(scheduler)
        self.db.add(scheduler_model)
        self.db.commit()
        self.db.refresh(scheduler_model)
        return scheduler_model.to_domain()

    def get_by_protocol(self, protocol: str) -> Scheduler:
        scheduler_model = (
            self.db.query(SchedulerModel).filter(SchedulerModel.protocol == protocol).first()
        )
        if scheduler_model is None:
            raise SchedulerNotFoundError(protocol=protocol)
        return scheduler_model.to_domain()
