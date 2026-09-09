class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tmp = set(nums)
        res = 1
        for num in nums:
            if num-1 not in tmp:
                continue
            tmptmp= num
            c = 1
            while tmptmp in tmp:
                tmptmp += 1
                c +=1
                res = max(c, res)
        return res
         