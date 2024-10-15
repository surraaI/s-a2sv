class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @functools.cache
        def dfs(val, rows_seen_mask):
            if val > 100:
                return 0

            best = 0
            best = max(best, dfs(val + 1, rows_seen_mask))

            for i in range(m):
                mask = 1 << i 
                if rows_seen_mask & mask:  
                    continue
                for j in range(n):
                    if val != grid[i][j]:
                        continue
                    new_mask = rows_seen_mask | mask  
                    best = max(best, val + dfs(val + 1, new_mask))
            return best

        return dfs(1, 0)  