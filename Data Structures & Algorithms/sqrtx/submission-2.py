class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        if x == 0:
            return x
        while l <= r:
            m = (l+r)//2
            if m * m == x:
                return m
            elif m*m < x:
                l = m + 1
            elif m*m > x:
                r = m - 1
        return (m if m*m < x else m-1)