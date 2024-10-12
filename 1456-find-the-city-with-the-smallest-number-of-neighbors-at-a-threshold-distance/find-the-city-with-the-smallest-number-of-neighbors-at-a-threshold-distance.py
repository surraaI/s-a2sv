class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
    
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        reachable_counts = []
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            reachable_counts.append(count)
        
        min_reachable = float('inf')
        result_city = -1
        for i in range(n):
            if reachable_counts[i] <= min_reachable:
                min_reachable = reachable_counts[i]
                result_city = i  
        
        return result_city