import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sortedStones = stones
        sortedStones.sort()
        while len(sortedStones) > 1:
            stone1, stone2 = sortedStones.pop(), sortedStones.pop()
            if stone1 > stone2:
                bisect.insort(sortedStones, stone1 - stone2)
            elif stone2 > stone1:
                bisect.insort(sortedStones, stone1 - stone2)
        return sortedStones[0] if sortedStones else 0