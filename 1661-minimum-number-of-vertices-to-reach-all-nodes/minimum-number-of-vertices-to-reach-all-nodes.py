class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges:
            indegree[u] = 0
            indegree[v] = 0

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        ans = []

        for key in indegree:
            if indegree[key] == 0:
                ans.append(key)
 
        return ans
