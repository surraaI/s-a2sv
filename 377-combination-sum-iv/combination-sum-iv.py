class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def dp(t):
            
            if t == 0:
                return 1
            
           
            if t in memo:
                return memo[t]
            
            
            count = 0
            for num in nums:
                if t >= num:
                    count += dp(t - num)
            
            
            memo[t] = count
            return count
        
        
        return dp(target)
