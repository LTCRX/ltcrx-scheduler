from typing import List

from core.domain.scheduler import Scheduler
from core.ports.scheduler_repository_port import SchedulerRepositoryPort

class SchedulerUseCase:

    def get_schedules_by_user(self, user_id: int) -> List[Scheduler]:
        return self.repository.get_by_user_id(user_id)