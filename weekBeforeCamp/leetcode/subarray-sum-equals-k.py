class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = { 0:1 }
        prefix_sum = [0] * (len(nums)+1)
        c = 0
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            if prefix_sum[i+1] - k  in d:
                c += d[prefix_sum[i+1]-k]
            d[prefix_sum[i+1]] = d.get(prefix_sum[i+1],0) + 1
        return c
        


