class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)<= 1:
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif stack and ((s[i] == ')' and stack.pop() != '(') or (s[i] == '}' and stack.pop() != '{') or (s[i] == ']' and stack.pop() != '[')):
                    return False       
        return True if not stack else False
        