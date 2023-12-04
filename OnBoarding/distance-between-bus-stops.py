class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        cl = 0
        if start > destination:
            start, destination = destination, start
        for i in range(start,destination):
            cl += distance[i]
     
        ant = 0
        for j in range(len(distance)-1, destination-1,-1):
            ant += distance[j]
        for k in range(start):
            ant += distance[k]
       
        return min(ant, cl)
