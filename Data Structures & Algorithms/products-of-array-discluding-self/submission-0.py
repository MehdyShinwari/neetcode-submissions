class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1, nums[0]]
        right = [1] * len(nums)
        right[len(nums)-2] = nums[len(nums)-1]
        for i in range(2, len(nums)):
            left.append(nums[i-1]*left[i-1])
        for i in range(len(nums)-3, -1, -1):
            right[i] = nums[i+1]*right[i+1]
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        return result