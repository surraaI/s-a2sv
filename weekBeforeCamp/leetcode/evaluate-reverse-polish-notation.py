class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '*':
                top1 = int(stack.pop())
                top2 = int(stack.pop())
                stack.append(top2 * top1)
            elif tokens[i] == '+':
                top1 = int(stack.pop())
                top2 = int(stack.pop())
                stack.append(top2 + top1)
            elif tokens[i] == '/':
                top1 = int(stack.pop())
                top2 = int(stack.pop())
                stack.append(top2 / top1)
            elif tokens[i] == '-':
                top1 = int(stack.pop())
                top2 = int(stack.pop())
                stack.append(top2 - top1)
            else:
                stack.append(tokens[i])
        return int(stack.pop())