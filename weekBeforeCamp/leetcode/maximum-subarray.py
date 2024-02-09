class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0]* (len(nums)+1)
        minimum = 0
        res = -float('inf')
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            res = max(prefix_sum[i+1] - minimum, res)
            minimum = min(minimum, prefix_sum[i+1])
        return res
        