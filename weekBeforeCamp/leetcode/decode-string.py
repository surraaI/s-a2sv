class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isnumeric():
                if stack and stack[-1].isnumeric():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
            elif s[i] == ']':
                temp = []
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                print(temp)
                temp = ''.join(temp[::-1])
                stack.append(temp * int(stack.pop()))
            else:
                stack.append(s[i])
            print(stack)
        return ''.join(stack)
                    
           
            