class TimeMap:

    def ub(self, arr, x):
        l, r = -1, len(arr)-1
        while l < r:
            m = (l+r+1)//2
            if arr[m] > x:
                r = m-1
            else:
                l = m
        return arr[l] if l >=0 else None

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
            i = self.ub(self.data1[key], timestamp)
            print(timestamp, self.data1[key][-1], key)
            if i:
                return self.data[i][key]
            elif timestamp > self.data1[key][-1]:
                return self.data[self.data1[key][-1]][key]
        return ""