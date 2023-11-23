from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from core.domain.scheduler import Scheduler
from core.domain.user import User


class RequestSchedulerInput(BaseModel):
    start_date: date = Field(..., description="Start date and time")
    end_date: date = Field(..., description="End date and time")
    quantity_samples: int = Field(..., description="Quantity of samples")
    number_of_scans: int = Field(..., description="Number of scans")
    protocol: str = Field(..., description="Number of protocol")
    voltage: Optional[float] = Field(None, description="Voltage value in volts")
    current: Optional[float] = Field(None, description="Current value in microamperes")
    filter: Optional[float] = Field(None, description="Filter value")
    resolution: Optional[float] = Field(None, description="Resolution value")

    def set_user(self, user: User):
        self.__user = user

    @property
    def user(self):
        return self.__user

    def to_domain(self) -> Scheduler:
        return Scheduler.create_request_scheduler(
            user=self.user,
            start_date=self.start_date,
            end_date=self.end_date,
            quantity_samples=self.quantity_samples,
            number_of_scans=self.number_of_scans,
            protocol=self.protocol,
            voltage=self.voltage,
            current=self.current,
            filter=self.filter,
            resolution=self.resolution,
        )


class RequestSchedulerOutput(BaseModel):
    protocol: str
