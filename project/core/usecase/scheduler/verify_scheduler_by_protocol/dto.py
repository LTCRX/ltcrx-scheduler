from dataclasses import asdict
from datetime import date
from pydantic import BaseModel, Field

from core.domain.scheduler import Scheduler


class VerifyByProtocolInput(BaseModel):
    protocol: str = Field(..., description="Number of protocol")


class VerifyByProtocolOutput(BaseModel):
    start_date: date
    end_date: date
    quantity_samples: int
    number_of_scans: int
    protocol: str
    voltage: float
    current: float
    filter: float
    resolution: float

    @classmethod
    def from_domain(cls, scheduler: Scheduler) -> "VerifyByProtocolOutput":
        return cls(**asdict(scheduler))
