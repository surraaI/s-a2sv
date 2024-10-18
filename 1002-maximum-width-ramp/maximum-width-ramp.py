class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ramp = 0
        stack = []
        
        
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                ramp = max(ramp, i - stack.pop())
        
        return ramp