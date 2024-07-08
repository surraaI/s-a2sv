class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        m = 0
        for i in range(1, len(nums)):
            m = max(m, nums[i] - nums[i-1])
        return m