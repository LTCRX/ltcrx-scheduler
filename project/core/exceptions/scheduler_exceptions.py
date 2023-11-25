from core.exceptions.not_found_exceptions import NotFoundError


class SchedulerNotFoundError(NotFoundError):
    def __init__(self, scheduler_id=None, protocol=None):
        self.scheduler_id = scheduler_id
        self.protocol = protocol
        message = "Scheduler not found"

        if scheduler_id:
            message += f" with ID: {scheduler_id}"
        if protocol:
            message += f" and protocol: {protocol}"

        super().__init__("Scheduler", message)
