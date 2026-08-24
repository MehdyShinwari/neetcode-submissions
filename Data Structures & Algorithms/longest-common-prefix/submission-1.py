class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mins = min(strs, key=len)
        for i, c in enumerate(mins):
            if any(s[i] != c for s in strs):
                return mins[:i]
        return mins