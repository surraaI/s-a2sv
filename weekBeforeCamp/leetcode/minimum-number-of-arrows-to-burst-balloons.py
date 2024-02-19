class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x:x[0])
        print(points)
        shootAt = points[0][1]
        c = 1
        for i in range(1,len(points)):
            xStart, xEnd = points[i]
            shootAt = min(shootAt, xEnd)
            if xStart > shootAt:
                c += 1
                shootAt = xEnd

        return c

