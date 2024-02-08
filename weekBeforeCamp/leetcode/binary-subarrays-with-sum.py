class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum= [0] * (len(nums)+1)
        d = {0:1}
        c = 0
        for i in range(1, len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            if prefix_sum[i] - goal in d:

                c += d[prefix_sum[i]-goal]
            d[prefix_sum[i]] = d.get(prefix_sum[i], 0 ) + 1
            
        return c
            
