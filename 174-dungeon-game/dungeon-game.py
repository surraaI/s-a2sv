class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0
    
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = dp[m-1][n] = 1  

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_health_needed = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, min_health_needed)

        return dp[0][0]