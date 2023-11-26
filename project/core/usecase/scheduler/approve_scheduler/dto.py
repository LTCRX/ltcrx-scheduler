from dataclasses import asdict
from datetime import date
from typing import Optional

from pydantic import BaseModel

from core.domain.scheduler import Scheduler


class ApproveSchedulerOutput(BaseModel):
    id: int
    start_date: date
    end_date: date
    message: Optional[str] = None

    @classmethod
    def from_domain(cls, scheduler: Scheduler) -> "ApproveSchedulerOutput":
        output = cls(**asdict(scheduler))
        output.message = f"scheduler {scheduler.protocol} approved successfully"
        return output
