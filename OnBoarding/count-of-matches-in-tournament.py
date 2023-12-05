class Solution:
    def numberOfMatches(self, n: int) -> int:
        p = n
        m = 0
        while p > 1:
            print(p)
            if p%2 != 0:
                m += (p-1)/2
                p = ((p-1)/2) + 1
            else:
                m += p/2
                p = p/2
            print(p, m)
        return int(m)