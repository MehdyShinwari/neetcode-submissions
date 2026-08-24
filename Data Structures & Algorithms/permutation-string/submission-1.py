class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        for ch in s1:
            freq_s1[ch] = freq_s1.get(ch, 0) +1
        l, r = 0, len(s1) -1
        freq_tmp = {}
        for ch in s2[:len(s1)]:
            freq_tmp[ch] = freq_tmp.get(ch, 0) +1
        while r < len(s2)-1:
            if freq_tmp == freq_s1:
                return True
            else:
                freq_tmp[s2[l]] -= 1
                if freq_tmp[s2[l]] == 0:
                    del freq_tmp[s2[l]]
                l += 1
                r += 1
                freq_tmp[s2[r]] = freq_tmp.get(s2[r], 0) +1
        if freq_tmp == freq_s1:
            return True
        return False
