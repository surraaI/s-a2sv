class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0 
        c =0
        while s and g:
            if s[0] >= g[0]:
                s.pop(0)
                g.pop(0)
                c += 1
            while s and g and s[0] < g[0]:
                s.pop(0)
        return c

