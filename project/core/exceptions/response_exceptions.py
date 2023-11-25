class ServerErrorResponse(Exception):
    status_code = 500

    def __init__(self, message="Internal Server Error"):
        self.message = message
        super().__init__(message)
