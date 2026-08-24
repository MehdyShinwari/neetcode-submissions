class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for x in s:
            if x in "([{":
                stack.append(x)
            elif x in ")]}":
                if not stack or stack[-1] != pairs[x]:
                    return False
                stack.pop()
        return stack == []
            