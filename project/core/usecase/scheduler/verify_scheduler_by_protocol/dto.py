from datetime import date
from pydantic import BaseModel, Field


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
