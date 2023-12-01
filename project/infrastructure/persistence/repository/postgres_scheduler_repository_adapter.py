from typing import List

from sqlalchemy.orm import Session
from sqlalchemy_filters import apply_filters, apply_sort

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

    def update(self, scheduler: Scheduler) -> Scheduler:
        scheduler_model = SchedulerModel.from_domain(scheduler)
        scheduler_model = self.db.merge(scheduler_model)
        self.db.commit()
        return scheduler_model.to_domain()

    def get_by_protocol(self, protocol: str) -> Scheduler:
        scheduler_model = (
            self.db.query(SchedulerModel).filter(SchedulerModel.protocol == protocol).first()
        )
        if scheduler_model is None:
            raise SchedulerNotFoundError(protocol=protocol)
        return scheduler_model.to_domain()

    def get_by_id(self, scheduler_id: int) -> Scheduler:
        scheduler_model = (
            self.db.query(SchedulerModel).filter(SchedulerModel.id == scheduler_id).first()
        )
        if scheduler_model is None:
            raise SchedulerNotFoundError(scheduler_id=scheduler_id)
        return scheduler_model.to_domain()

    def get_all(
        self, filters_dict: List[dict] = None, order_dict: List[dict] = None
    ) -> List[Scheduler]:
        query = self.db.query(SchedulerModel)
        if filters_dict:
            query = apply_filters(query, filters_dict)
        if order_dict:
            query = apply_sort(query, order_dict)
        schedulers_model = query.all()
        return [scheduler_model.to_domain() for scheduler_model in schedulers_model]

    def get_all_by_user(self, user_id: int) -> List[Scheduler]:
        scheduler_models = (
            self.db.query(SchedulerModel).filter(SchedulerModel.user_id == user_id).all()
        )
        return [Scheduler.from_domain(model) for model in scheduler_models]
