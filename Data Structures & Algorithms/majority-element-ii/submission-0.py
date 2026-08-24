class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = dict()
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for x in count:
            if count[x] > (len(nums)/3):
                res.append(x)
        return res