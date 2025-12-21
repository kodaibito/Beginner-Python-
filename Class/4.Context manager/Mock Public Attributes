class mock:
    def __init__(self, obj, **mocks):
        self.obj = obj
        self.mocks = mocks
        self.originals = {}

    def __enter__(self):
        for attr, val in self.mocks.items():
            self.originals[attr] = getattr(self.obj, attr)
            setattr(self.obj, attr, val)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        for attr, val in self.originals.items():
            setattr(self.obj, attr, val)