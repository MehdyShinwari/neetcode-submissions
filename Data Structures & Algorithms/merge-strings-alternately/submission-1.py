class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res = res + word1[i] + word2[i]
        big = ""
        if len(word1) > len(word2):
            big = word1
        else:
            big = word2
        return res + big[i+1:]