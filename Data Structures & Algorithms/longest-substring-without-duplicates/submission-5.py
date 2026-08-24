class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        kek = set()
        i = 0
        j = 0
        biggest = 0
        while j<len(s):
            if s[j] not in kek:
                kek.add(s[j])
                j += 1
                biggest = max(biggest, j - i) 
            else:
                kek.remove(s[i])
                i += 1
        return biggest