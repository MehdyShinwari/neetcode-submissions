class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        begin = 0
        end = len(nums)-1
        for i in range(len(nums)):
            if i > end:
                return
            if nums[i]==0:
                nums[begin],nums[i] = nums[i], nums[begin]
                begin += 1
                i -= 1
            elif nums[i]==2:
                nums[end],nums[i] = nums[i], nums[end]
                end -= 1
                i -= 1
            elif nums[i]==1:
                nums[int(len(nums)/2)], nums[i] = nums[i], nums[int(len(nums)/2)]
                i -= 1