from sqlalchemy.orm import Session

from core.domain.scheduler import Scheduler
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