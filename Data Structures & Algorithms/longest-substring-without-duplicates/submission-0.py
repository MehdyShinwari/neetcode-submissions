class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)-1):
            longest = max(len(set(s[:i])),longest)
        
        return longest
