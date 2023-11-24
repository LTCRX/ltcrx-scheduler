from datetime import date

from core.domain.scheduler import Scheduler
from pydantic import BaseModel, Field


class VerifyByProtocolInput(BaseModel):
    protocol: str = Field(..., description="Number of protocol")

    def to_domain(self) -> Scheduler:
        return Scheduler.create_request_scheduler(
            protocol=self.protocol
        )


class VerifyByProtocolOutput(BaseModel):
    start_date: date
    end_date: date
    quantity_samples:int
    number_of_scans: int
    protocol: str
    voltage: float
    current: float
    filter: float
    resolution: float
