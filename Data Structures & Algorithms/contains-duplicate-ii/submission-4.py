class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i, n in enumerate(nums):
            freq.setdefault(n, []).append(i)
        for x in freq:
            print(x, len(freq[x]))
            if len(freq[x]) >=2  and abs(freq[x][0] - freq[x][1])<=k:
                return True
        return False

            
