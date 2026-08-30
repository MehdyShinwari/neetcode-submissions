class FreqStack:

    def __init__(self):
        self.stack = {}
        self.freqs = {}
        self.maxCnt = 0

    def push(self, val: int) -> None:
        freqCnt = self.freqs.get(val, 0) + 1
        self.freqs[val] = freqCnt
        if freqCnt > self.maxCnt:
            self.maxCnt = freqCnt
            self.stack[freqCnt] = []
        self.stack[freqCnt].append(val)

    def pop(self) -> int:
        tmp = self.stack[self.maxCnt].pop()
        self.freqs[tmp] -= 1
        if not self.stack[self.maxCnt]:
            self.maxCnt -=1
        return tmp

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()