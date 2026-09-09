class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[timestamp] = {key: value}

    def get(self, key: str, timestamp: int) -> str:
        while timestamp not in self.data:
            timestamp -= 1
        return self.data[timestamp][key] if self.data[timestamp][key] else ""
