class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dp = [[float('inf')] * n for i in range(n)]
        dp[0][k-1] = 0

        for i in range(1,n):
            dp[i][k-1] = 0
            for u, v, w in times:
                dp[i][v-1] = min(dp[i][v-1], dp[i-1][u-1] + w)
        
        res = max(dp[-1])

        return res if res != float('inf') else -1

        