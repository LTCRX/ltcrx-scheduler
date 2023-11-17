import uuid

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from core.domain.scheduler import Scheduler
from core.domain.scheduler_status import SchedulerStatusEnum
from infrastructure.persistence.models.base import Base


class SchedulerModel(Base):
    __tablename__ = "schedulers"

    id = Column(Integer, primary_key=True)
    protocol = Column(String, nullable=False, default=str(uuid.uuid4()), unique=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    quantity_samples = Column(Integer, nullable=False)
    number_of_scans = Column(Integer, nullable=False)
    voltage = Column(Float, nullable=True)
    current = Column(Float, nullable=True)
    filter = Column(Float, nullable=True)
    resolution = Column(Float, nullable=True)

    user = relationship("UserModel", back_populates="schedulers")

    def to_domain(self) -> Scheduler:
        return Scheduler(
            id=self.id,
            protocol=self.protocol,
            user=self.user,
            status=SchedulerStatusEnum.get_from_string(self.status),
            start_date=self.start_date,
            end_date=self.end_date,
            quantity_samples=self.quantity_samples,
            number_of_scans=self.number_of_scans,
            voltage=self.voltage,
            current=self.current,
            filter=self.filter,
            resolution=self.resolution,
        )

    @classmethod
    def from_domain(cls, scheduler: Scheduler) -> "SchedulerModel":
        fields = dict(
            user_id=scheduler.user.id,
            status=scheduler.status.name,
            start_date=scheduler.start_date,
            end_date=scheduler.end_date,
            quantity_samples=scheduler.quantity_samples,
            number_of_scans=scheduler.number_of_scans,
            voltage=scheduler.voltage,
            current=scheduler.current,
            filter=scheduler.filter,
            resolution=scheduler.resolution,
        )
        return cls(**fields)
