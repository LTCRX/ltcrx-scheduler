from core.exceptions.entity_exceptions import EntityNotFoundError


class SchedulerNotFoundError(EntityNotFoundError):
    def __init__(self, scheduler_id=None, protocol=None):
        self.scheduler_id = scheduler_id
        self.protocol = protocol
        message = "Scheduler not found"

        if scheduler_id:
            message += f" with ID: {scheduler_id}"
        if protocol:
            message += f" and protocol: {protocol}"

        super().__init__("Scheduler", message)
