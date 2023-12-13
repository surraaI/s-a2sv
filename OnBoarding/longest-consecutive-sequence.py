class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
      
        maxleng = 1
      
        if len(nums)<1:
            return 0
        stack = []
       
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
                maxleng =max(maxleng, len(stack))
            elif stack and nums[i] == stack[-1] + 1:
                stack.append(nums[i])
                maxleng =max(maxleng, len(stack))

            elif stack and nums[i] > stack[-1] + 1:
                maxleng =max(maxleng, len(stack))
                stack.clear()
                stack.append(nums[i])
            else:
                continue
            
            
            
        
            
                

            
        return maxleng