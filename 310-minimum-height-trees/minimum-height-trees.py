class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
       
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        def bfs(start):
            visited = [False] * n
            queue = deque([start])
            visited[start] = True
            dist = -1
            farthest_node = start
            
            while queue:
                dist += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    farthest_node = node
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
            
            return farthest_node, dist
        
        
        endpoint1, _ = bfs(0)
        
        
        endpoint2, _ = bfs(endpoint1)
        
        
        def find_path(start, end):
            queue = deque([(start, [start])])
            visited = [False] * n
            visited[start] = True
            
            while queue:
                node, path = queue.popleft()
                if node == end:
                    return path
                
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, path + [neighbor]))
        
        path = find_path(endpoint1, endpoint2)
        path_len = len(path)
        
        
        if path_len % 2 == 0:
            return [path[path_len // 2 - 1], path[path_len // 2]]
        else:
            return [path[path_len // 2]]