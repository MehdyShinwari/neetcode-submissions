class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            match x:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    tmp1 = stack.pop()
                    tmp2 = stack.pop()
                    stack.append(tmp2 - tmp1)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    tmp1 = stack.pop()
                    tmp2 = stack.pop()
                    stack.append(int(tmp2/tmp1))
                case _:
                    stack.append(int(x))
        return stack[0]