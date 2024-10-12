class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Mark direct prerequisites
        for pre, course in prerequisites:
            reachable[pre][course] = True
        
        # Step 2: Floyd-Warshall to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        # Step 3: Answer each query
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        
        return result

            