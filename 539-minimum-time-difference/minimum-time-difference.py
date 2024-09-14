class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToMinutes(time):
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        

        for i in range(len(timePoints)):
            timePoints[i] = timeToMinutes(timePoints[i])
        
        timePoints.sort()
        m = float('inf')

        for i in range(1, len(timePoints)):
            m = min(m, timePoints[i] - timePoints[i-1])
        
        circularDifference = (24 * 60) - (timePoints[-1] - timePoints[0])
        m = min(m, circularDifference)
        
        return m

