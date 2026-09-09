class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hold = 0
        for i in range(len(nums)):
            print(i,k, (i+k)%k)
            hold = nums[(i+k)%k]
            nums[(i+k)%k] = nums[i]
            nums[i] = hold
