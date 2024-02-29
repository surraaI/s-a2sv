class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)< 2:
            return ''
        s_set = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s1 if len(s1) >= len(s2) else s2
        return s