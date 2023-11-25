class NotFoundError(Exception):
    def __init__(self, entity_name, message=None):
        self.entity_name = entity_name
        if message is None:
            message = f"Entity {self.entity_name} not found"
        super().__init__(message)
