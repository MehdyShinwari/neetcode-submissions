class TimeMap:

    def __init__(self):
        self.data = {}
        self.last = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[timestamp] = {key: value}
        self.last = timestamp

    def get(self, key: str, timestamp: int) -> str:
        if timestamp not in self.data:
            if timestamp < self.last:
                return ""
            return self.data[self.last][key] if self.data[self.last][key] else ""
        return self.data[timestamp][key] if self.data[timestamp][key] else ""
