class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for q in times:
            graph[q[0]].append((q[1],q[2]))
        
        time = {node: float('inf') for node in range(1, n+1)}
        time[k] = 0
        processed = set()

        heap = [(k, 0)]
        while heap:
            curr, t = heapq.heappop(heap)
            
            for child, weight in graph[curr]:
                if t + weight < time[child]:
                    time[child] = t + weight
                    heapq.heappush(heap, (child, time[child]))

        ans = 0
        
        for node in time:
            if time[node] == float('inf'):
                return -1
            ans = max(time[node], ans)

        return ans
        
            