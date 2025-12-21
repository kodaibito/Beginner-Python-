import logging

class SuppressAndLog:
    def __init__(self, *errors):
        self.errors = errors

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.errors):
            logging.error(f"Error suppressed: {exc_val}")
            return True  # hatayı bastır
        return False