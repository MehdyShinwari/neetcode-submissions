class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_replace = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i -1]:
                nums[cur_replace] = nums[i]
                cur_replace +=1
        return cur_replace
            