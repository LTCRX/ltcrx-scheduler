from typing import List

from core.domain.scheduler import Scheduler
from core.usecase.scheduler.get_all_scheduler.dto import FiltersInput
from core.usecase.usecase_interface import UseCaseInterface
from sqlalchemy.orm import Session
from infrastructure.persistence.repository.postgres_scheduler_repository_adapter import (
    PostgresSchedulerRepositoryAdapter,
)


class GetAllSchedulerUseCase(UseCaseInterface):
    def __init__(self, db: Session):
        self.repository = PostgresSchedulerRepositoryAdapter(db)

    order_dict = [{"model": "SchedulerModel", "field": "start_date", "direction": "asc"}]

    def execute(self, filters: FiltersInput) -> List[Scheduler]:
        return self.repository.get_all(filters.to_filters_dict(), self.order_dict)
