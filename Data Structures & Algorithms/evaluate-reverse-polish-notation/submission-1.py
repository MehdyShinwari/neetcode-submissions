class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            match x:
                case "+":
                    tmp = stack[0] + stack[1]
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                case "-":
                    tmp = stack[0] - stack[1]
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                case "*":
                    tmp = stack[0] * stack[1]
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                case "/":
                    tmp = int(stack[0] / stack[1])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                case _:
                    stack.append(int(x))
        return stack[0]