class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        d = {}
        r = l = 0
        m = 0
        while r < len(nums):
            d[nums[r]] = d.get(nums[r], 0 ) + 1
            while 0 in d and d[0] > k and l < len(nums):
                
                if nums[l] == 0:
                    d[0] -= 1
                l += 1
            m = max(m, r-l+1)
            r += 1
            
            
        return m