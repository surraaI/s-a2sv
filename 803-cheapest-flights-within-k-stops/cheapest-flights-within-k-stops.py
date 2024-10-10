class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float('inf')] * n
        curr = [float('inf')] * n
       
        prev[src] = 0
        curr[src] = 0

        for i in range(k+1):
            for u, v, w in flights:
                curr[v] = min(curr[v], prev[u] + w)

            prev = curr[:]

        
        res = curr[dst]
        

        return res if res != float('inf') else -1