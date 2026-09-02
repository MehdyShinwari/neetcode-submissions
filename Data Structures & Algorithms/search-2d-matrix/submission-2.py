class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) -1
        n = len(matrix[0])-1

        while l<=r :
            m = (l+r) // 2
            if matrix[m][0] <= target:
                if matrix[m][n] >= target:
                    ll, rr = 0, n
                    while ll <= rr:
                        mm = (ll+rr)//2
                        if matrix[m][mm] == target:
                            return True
                        elif matrix[m][mm] < target:
                            ll = mm + 1
                        elif matrix[m][mm] > target:
                            rr = mm -1
                    return False
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
        return False
