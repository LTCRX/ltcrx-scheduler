from abc import ABC, abstractmethod
from typing import List

from core.domain.scheduler import Scheduler


class SchedulerRepositoryPort(ABC):
    @abstractmethod
    def save(self, scheduler: Scheduler) -> Scheduler:
        pass

    @abstractmethod
    def update(self, scheduler: Scheduler) -> Scheduler:
        pass

    @abstractmethod
    def get_by_protocol(self, protocol: str) -> Scheduler:
        pass

    @abstractmethod
    def get_by_id(self, scheduler_id: int) -> Scheduler:
        pass

    @abstractmethod
    def get_all(self, filters_dict: List[dict], order_dict: List[dict]) -> List[Scheduler]:
        pass
