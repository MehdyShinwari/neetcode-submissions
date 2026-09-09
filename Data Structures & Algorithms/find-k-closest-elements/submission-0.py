class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k-1
        curMin = float('inf')
        res = arr[:k]
        curSum = sum(arr[:k])
        while r < len(arr) - 1:
            if (curSum/k) - x < curMin:
                curMin = (curSum/k) - x
                curSum = curSum - arr[l]
                del res[0]
                l += 1
                r += 1
                curSum = curSum + arr[r]
                res.append(arr[r])
            else:
                break
        return res


        