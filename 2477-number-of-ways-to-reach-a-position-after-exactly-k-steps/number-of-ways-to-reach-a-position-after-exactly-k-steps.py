class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        endPos -= startPos

        @cache
        def dp(x, left):
            if left == 0:
                if x == 0:
                    return 1
                return 0
            
            return (dp(x+1, left - 1) + dp(x-1, left - 1))%MOD

        return dp(endPos,k) % MOD

        