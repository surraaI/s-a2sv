class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        ans = 0
        
        for i in range(k):
            ans += m
            m += 1
        
        return ans
        