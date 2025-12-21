from copy import deepcopy

class TransactionalSaver:
    def __init__(self, obj):
        self.original = deepcopy(obj)
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.obj.__dict__ = self.original.__dict__
        return False  # hatayı bastırma
    class Data:
        def __init__(self, value):
            self.value = value
