class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def area(x,y):
            return min(heights[x], heights[y]) * (y-x)
        x = 0
        y = len(heights) -1
        max_area = 0
        while x < y:
            ar = area(x,y)
            max_area = max(max_area, ar)
            if heights[x]<=heights[y]:
                x += 1
            else:
                y -= 1
        return max_area
