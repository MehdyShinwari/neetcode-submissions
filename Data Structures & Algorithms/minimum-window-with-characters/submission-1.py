class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs_t = {}
        for ch in t:
            freqs_t[ch] = freqs_t.get(ch, 0) + 1
        req = len(freqs_t)
        satisfied = 0
        l=0
        freqs_window = {}
        best_len = float('inf')
        best_l, best_r = 0, 0
        for r in range(len(s)):
            freqs_window[s[r]] = freqs_window.get(s[r], 0) + 1
            if s[r] in freqs_t and freqs_window[s[r]] == freqs_t[s[r]]:
                satisfied += 1
            while req == satisfied:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l, best_r = l, r
                freqs_window[s[l]] -=1
                if s[l] in freqs_t and freqs_window[s[l]] < freqs_t[s[l]]:
                    satisfied -=1
                l += 1
        return s[best_l:best_r+1] if best_len != float('inf') else ""



