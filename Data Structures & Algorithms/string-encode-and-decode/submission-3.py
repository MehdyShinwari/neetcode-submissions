class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s.find("#") != -1:
            cur2 = s.find("#")
            cur3 = int(s[0:cur2])
            res.append(s[cur2+1:cur3+cur2+1])
            s = s[cur2+cur3+1:]
        return res
