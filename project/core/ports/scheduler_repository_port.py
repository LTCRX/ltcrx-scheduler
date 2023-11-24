from abc import ABC, abstractmethod

from core.domain.scheduler import Scheduler


class SchedulerRepositoryPort(ABC):
    @abstractmethod
    def save(self, scheduler: Scheduler) -> Scheduler:
        pass

    @abstractmethod
    def get_by_protocol(self, protocol: str) -> Scheduler:
        pass
