class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minArray = len(nums) + 1
        l, r = 0, 0
        tmp_sum = nums[l] 
        while r < len(nums)-1:
            if tmp_sum < target:
                r += 1
                tmp_sum += nums[r]
            else:
                minArray = min(minArray, r - l + 1)
                tmp_sum -= nums[l]
                l += 1
        while tmp_sum >= target:
            minArray = min(minArray, r - l + 1)
            tmp_sum -= nums[l]
            l += 1
        if minArray == len(nums)+1:
            return 0
        return minArray