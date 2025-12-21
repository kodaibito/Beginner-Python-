class CacheManager:
    cache = {}

    def __init__(self, key, compute_func):
        self.key = key
        self.compute_func = compute_func

    def __enter__(self):
        if self.key in CacheManager.cache:
            return CacheManager.cache[self.key]
        self.result = self.compute_func()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        CacheManager.cache[self.key] = self.result