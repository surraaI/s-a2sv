class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = 0
        swaps = 0
        for i in range(len(s)-1, -1,-1):
            if s[i] == '0':
                zeros += 1
            else:
                swaps += zeros
        return swaps
