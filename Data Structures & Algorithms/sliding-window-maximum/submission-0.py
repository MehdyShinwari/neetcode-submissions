class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k-1
        while r < len(nums):
            tmp= max(nums[l:r+1])
            res.append(tmp)
            l += 1
            r += 1
        return res