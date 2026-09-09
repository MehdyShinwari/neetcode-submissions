class TimeMap:

    def __init__(self):
        self.data = {}
        self.data1 = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[timestamp] = {key: value}
        self.data1.setdefault(key, []).append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.data:
            if key in self.data[timestamp]:
                return self.data[timestamp][key]
        elif key in self.data1:
            return self.data[self.data1[key][-1]][key] if timestamp >self.data1[key][-1] else ""
        return ""
