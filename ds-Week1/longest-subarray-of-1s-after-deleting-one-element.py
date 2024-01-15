class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        m = 0
        d = {}
        if 0 not in nums:
            return len(nums) - 1
        while r < len(nums):
            d[nums[r]] = d.get(nums[r], 0 ) + 1
            while 0 in d and d[0] > 1 and l < len(nums):
                if nums[l] == 0:
                    d[0] -= 1
                l += 1
            m = max(m, r-l)
            r += 1
        return m
                

                
        