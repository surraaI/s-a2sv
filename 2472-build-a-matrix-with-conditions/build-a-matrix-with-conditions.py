class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        rowGraph = defaultdict(list)
        for u, v in rowConditions:
            rowGraph[u].append(v)
            
        colGraph = defaultdict(list)
        for u, v in colConditions:
            colGraph[u].append(v)
        
        def topoSort(graph):
            inDegree = {i: 0 for i in range(1, k + 1)}
            for u in graph:
                for v in graph[u]:
                    inDegree[v] += 1
            queue = deque([i for i in inDegree if inDegree[i] == 0])
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for v in graph[node]:
                    inDegree[v] -= 1
                    if inDegree[v] == 0:
                        queue.append(v)
            return order if len(order) == k else []
        
        rowOrder = topoSort(rowGraph)
        colOrder = topoSort(colGraph)
        
        if not rowOrder or not colOrder:
            return []
        
        rowMap = {num: i for i, num in enumerate(rowOrder)}
        colMap = {num: i for i, num in enumerate(colOrder)}
        
        result = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            result[rowMap[i]][colMap[i]] = i
        
        return result
        