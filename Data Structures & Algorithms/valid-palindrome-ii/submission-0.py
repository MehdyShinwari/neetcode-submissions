class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        skip = True
        while l < int(len(s)/2):
            if s[l] != s[r]:
                if skip:
                    skip = False
                    if s[l+1] == s[r]:
                        l = l+2
                        r= r-1
                        continue
                    if s[l] == s[r-1]:
                        l = l+1
                        r = r-2
                        continue
                return False
            l = l+1
            r = r-1
        return True