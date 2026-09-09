class TimeMap:

    def lb(self, arr, x):
        l, r = 0, len(arr)
        while l < r:
            m = (l+r)//2
            if arr[m] < x:
                l = m+1
            else:
                r = m
        return arr[l] if l < len(arr) else None

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
            i = self.lb(self.data1[key], timestamp)
            print(i)
            if i:
                    return self.data[i][key]
            else:
                return self.data[self.data1[key][-1]][key]
        return ""