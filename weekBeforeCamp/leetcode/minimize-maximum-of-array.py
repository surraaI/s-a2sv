class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = prefix = nums[0]
        for i in range(1, len(nums)):
            prefix += nums[i]
            res = max(res, math.ceil(prefix/(i+1)))
        return res
    