from enum import Enum


class SchedulerStatusEnum(str, Enum):
    PENDING = "Aguardando aprovação"
    REJECTED = "Rejeitado"
    ACCEPTED = "Aceito"
    CANCELED = "Cancelado"

    @classmethod
    def get_from_string(cls, status_string: str) -> "SchedulerStatusEnum":
        for status_enum in cls:
            if status_enum.name.lower() == status_string.lower():
                return status_enum
        raise ValueError(f"No matching enum member for string: {status_string}")
