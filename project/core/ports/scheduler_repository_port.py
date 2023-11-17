from abc import ABC, abstractmethod

from core.domain.scheduler import Scheduler


class SchedulerRepositoryPort(ABC):
    @abstractmethod
    def save(self, scheduler: Scheduler) -> Scheduler:
        pass
