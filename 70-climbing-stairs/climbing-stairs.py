class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(n):
            if n <= 2:
                return n
            return climb(n-1) + climb(n-2)
        
        return climb(n)

        
        
