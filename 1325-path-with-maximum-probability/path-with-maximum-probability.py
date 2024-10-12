class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        
        pq = [(-1, start_node)]  
        maxProb = [0] * n
        maxProb[start_node] = 1

        
        while pq:
            currProb, node = heapq.heappop(pq)
            currProb = -currProb  

            if node == end_node:
                return currProb 

          
            for neighbor, edgeProb in graph[node]:
                newProb = currProb * edgeProb
                if newProb > maxProb[neighbor]:
                    maxProb[neighbor] = newProb
                    heapq.heappush(pq, (-newProb, neighbor))

        return 0.0