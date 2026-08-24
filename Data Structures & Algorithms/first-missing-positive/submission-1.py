class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        tmp = set(nums)
        for i in range(1, len(nums)+1):
            if i not in tmp:
                return i
        return len(nums)+1