class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        c = 0
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    c += 1
                else:
                    stack.pop()
        return c + len(stack)


        