from datetime import date
from typing import List

from pydantic import BaseModel, Field

from core.domain.scheduler import Scheduler
from core.domain.scheduler_status import SchedulerStatusEnum


class GetSchedulesByUserOutput(BaseModel):
    protocol: str = Field(..., description="scheduler protocol")
    status: SchedulerStatusEnum = Field(..., description="scheduler status")
    start_date: date = Field(..., description="Start date and time")
    end_date: date = Field(..., description="End date and time")

    @classmethod
    def from_domain(cls, schedules: List[Scheduler]) -> List["GetSchedulesByUserOutput"]:
        outputs = []
        for schedule in schedules:
            output = cls(
                protocol=schedule.protocol,
                status=schedule.status,
                start_date=schedule.start_date,
                end_date=schedule.end_date,
            )
            outputs.append(output)
        return outputs

