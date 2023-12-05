class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        t = 0
        for i in range(len(points)-1):
            
            t += max(abs(points[i+1][0]-points[i][0]), abs(points[i][1] - points[i+1][1]))
            
        return t