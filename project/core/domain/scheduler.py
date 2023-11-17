from datetime import datetime

from typing import Optional
from dataclasses import dataclass

from core.domain.scheduler_status import SchedulerStatusEnum
from core.domain.user import User


@dataclass
class Scheduler:
    user: User
    status: SchedulerStatusEnum
    start_date: datetime
    end_date: datetime
    quantity_samples: int
    number_of_scans: int
    id: Optional[int] = None
    protocol: Optional[str] = None
    voltage: Optional[float] = None
    current: Optional[float] = None
    filter: Optional[float] = None
    resolution: Optional[float] = None

    @classmethod
    def create_request_scheduler(
        cls,
        user: User,
        start_date: datetime,
        end_date: datetime,
        quantity_samples: int,
        number_of_scans: int,
        voltage: Optional[float] = None,
        current: Optional[float] = None,
        filter: Optional[float] = None,
        resolution: Optional[float] = None,
    ) -> "Scheduler":
        return cls(
            user=user,
            status=SchedulerStatusEnum.PENDING,
            start_date=start_date,
            end_date=end_date,
            quantity_samples=quantity_samples,
            number_of_scans=number_of_scans,
            voltage=voltage,
            current=current,
            filter=filter,
            resolution=resolution,
        )
