from dataclasses import asdict
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from core.domain.scheduler import Scheduler
from core.domain.scheduler_status import SchedulerStatusEnum


class FiltersInput(BaseModel):
    user_id: Optional[int] = Field(None, description="user id")
    status: Optional[SchedulerStatusEnum] = Field(None, description="scheduler status")
    start_date: Optional[date] = Field(None, description="Start date and time")

    def to_filters_dict(self):
        _start_date = self.start_date or datetime.now().date()
        _status = self.status.name if self.status else None
        filters = [
            {"field": "user_id", "op": "==", "value": self.user_id},
            {"field": "status", "op": "==", "value": _status},
            {"field": "start_date", "op": ">=", "value": _start_date},
        ]
        return [f for f in filters if f["value"] is not None]


class GetAllSchedulerOutput(BaseModel):
    id: int = Field(..., description="scheduler id")
    user_name: str = Field(None, description="user name")
    user_email: str = Field(None, description="user email")
    status: SchedulerStatusEnum = Field(..., description="scheduler status")
    start_date: date = Field(..., description="Start date and time")
    end_date: date = Field(..., description="End date and time")

    @classmethod
    def from_domain(cls, schedulers: List[Scheduler]) -> List["GetAllSchedulerOutput"]:
        outputs = []
        for scheduler in schedulers:
            output = cls(**asdict(scheduler))
            output.user_name = scheduler.user.username
            output.user_email = scheduler.user.email
            outputs.append(output)
        return outputs
