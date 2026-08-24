class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tmp = set(nums)
        res = 0
        for num in tmp:
            if num-1 not in tmp:
                length = 1
                while (num+length) in tmp:
                    length += 1
                res = max(length, res)
        return res
         