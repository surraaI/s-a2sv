class Solution:
    def lengthLongestPath(self, input: str) -> int:

        stack = [0]
        lines = input.split("\n")
        max_len = 0
        
        for i in range(len(lines)):
            level = lines[i].count('\t')
            while level < len(stack) - 1:
                stack.pop()
            stack.append(len(lines[i]) - level + 1 + stack[-1])
            if '.' in lines[i]:
                max_len = max(max_len, stack[-1] - 1)
        
        return max_len

        
        return -1
        