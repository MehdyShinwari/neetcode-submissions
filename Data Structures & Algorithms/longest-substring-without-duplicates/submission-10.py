class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        currSet = set()
        maxLen = 0
        while j < len(s):
            if s[j] not in currSet:
                currSet.add(s[j])
                maxLen = max(maxLen, len(currSet))
                j += 1
            else:
                i += 1
                currSet = set()
                currSet.update(s[i:j])
        return maxLen