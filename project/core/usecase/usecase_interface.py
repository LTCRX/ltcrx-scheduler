from abc import ABC, abstractmethod
from pydantic import BaseModel


class UseCaseInterface(ABC):
    @abstractmethod
    def execute(self, command_input: BaseModel) -> BaseModel:
        pass
