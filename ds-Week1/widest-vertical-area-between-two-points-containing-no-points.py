class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xi = [x[0] for x in points]
        xi.sort()
        m = 0
        for i in range(len(xi)-1):
            m = max(xi[i+1]-xi[i], m)
        return m

        