class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        memo = {}
        def dp(i, target):

            if i >= n or target <= 0:
                return target == 0
            
            if (i, target) not in memo:
                memo[(i,target)] = dp(i+1, target - nums[i]) or dp(i+1, target)
            
            return memo[(i,target)]
            

        
        return sum(nums)%2 == 0 and dp(0, sum(nums)//2)


        