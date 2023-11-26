from dataclasses import asdict
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from core.domain.scheduler import Scheduler


class VerifyByProtocolInput(BaseModel):
    protocol: str = Field(..., description="Number of protocol")


class VerifyByProtocolOutput(BaseModel):
    start_date: date = Field(..., description="Start date and time")
    end_date: date = Field(..., description="End date and time")
    quantity_samples: int = Field(..., description="Quantity of samples")
    number_of_scans: int = Field(..., description="Number of scans")
    voltage: Optional[float] = Field(None, description="Voltage value in volts")
    current: Optional[float] = Field(None, description="Current value in microamperes")
    filter: Optional[float] = Field(None, description="Filter value")
    resolution: Optional[float] = Field(None, description="Resolution value")

    @classmethod
    def from_domain(cls, scheduler: Scheduler) -> "VerifyByProtocolOutput":
        return cls(**asdict(scheduler))
