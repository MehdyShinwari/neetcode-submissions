class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if not stack:
                stack.append(x)
            else:
                if stack[-1] * x > 0:
                    stack.append(x)
                else:
                    tmp = 0
                    while stack and abs(x) > abs(stack[-1]) and stack[-1] * x < 0:
                        tmp = stack.pop()
                    if abs(x) > abs(tmp):
                        stack.append(x)
                    elif abs(tmp) > abs(x):
                        stack.append(tmp)
        return stack
                    