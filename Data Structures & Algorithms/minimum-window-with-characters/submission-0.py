class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs_t = {}
        for ch in t:
            freqs_t[ch] = freqs_t.get(ch, 0) + 1
        l=0
        freqs_window = {}
        best_len = float('inf')
        best_l, best_r = 0, 0
        for r in range(len(s)):
            freqs_window[s[r]] = freqs_window.get(s[r], 0) + 1
            while freqs_t.items() <= freqs_window.items():
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l, best_r = l, r
                freqs_window[s[l]] -=1
                if freqs_window[s[l]] == 0:
                    del freqs_window[s[l]]
                l += 1
        
        return s[best_l:best_r+1] if best_len != float('inf') else ""



