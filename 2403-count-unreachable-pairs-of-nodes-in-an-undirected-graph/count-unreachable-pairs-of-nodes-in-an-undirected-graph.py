class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def bfs(start, visited, graph):
            queue = deque([start])
            visited[start] = True
            size = 0
            while queue:
                node = queue.popleft()
                size += 1
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return size
            
       
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        visited = [False] * n
        component_sizes = []
        
        for i in range(n):
            if not visited[i]:
                size = bfs(i, visited, graph)
                component_sizes.append(size)
        
        
        total_pairs = n * (n - 1) // 2
        reachable_pairs = 0
        
        for size in component_sizes:
            reachable_pairs += size * (size - 1) // 2
        
        unreachable_pairs = total_pairs - reachable_pairs
        return unreachable_pairs