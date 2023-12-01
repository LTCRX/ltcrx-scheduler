from dataclasses import asdict
from datetime import date
from typing import List

from pydantic import BaseModel, Field

from core.domain.scheduler import Scheduler
from core.domain.scheduler_status import SchedulerStatusEnum


class GetAllSchedulerByUserOutput(BaseModel):
    protocol: str = Field(..., description="scheduler id")
    status: SchedulerStatusEnum = Field(..., description="scheduler status")
    start_date: date = Field(..., description="Start date and time")
    end_date: date = Field(..., description="End date and time")

    @classmethod
    def from_domain(cls, schedulers: List[Scheduler]) -> List["GetAllSchedulerByUserOutput"]:
        outputs = []
        for scheduler in schedulers:
            output = cls(**asdict(scheduler))
            outputs.append(output)
        return outputs
