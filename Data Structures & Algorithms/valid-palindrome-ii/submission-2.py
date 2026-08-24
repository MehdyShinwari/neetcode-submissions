class Solution:
    def validPalindrome(self, s: str) -> bool:
      def is_pal(lo, hi):
          while lo < hi:
              if s[lo] != s[hi]:
                  return False
              lo += 1
              hi -= 1
          return True

      l, r = 0, len(s) - 1
      while l < r:
          if s[l] != s[r]:
              return is_pal(l + 1, r) or is_pal(l, r - 1)
          l += 1
          r -= 1
      return True