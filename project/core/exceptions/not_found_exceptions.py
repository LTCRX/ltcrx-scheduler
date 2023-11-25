class NotFoundError(Exception):
    def __init__(self, entity_name):
        self.entity_name = entity_name
        super().__init__(f"Entity '{entity_name}' not found")
