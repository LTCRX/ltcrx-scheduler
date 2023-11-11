from abc import ABC, abstractmethod
from typing import Any
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from datetime import datetime


@as_declarative()
class Base:
    id: Any
    __name__: str

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def to_domain(self):
        raise NotImplementedError("to_domain")

    def from_domain(self):
        raise NotImplementedError("from_domain")

