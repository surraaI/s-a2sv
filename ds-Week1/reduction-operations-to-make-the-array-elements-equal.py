class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        temp = sorted(set(nums))
        nums = sorted(nums)
       
        count = {}
        for i in range(len(nums)):
            
            count[nums[i]] = count.get(nums[i],0) + 1
        c = 0
        r = 1
        for i in range(1, len(temp)):
            c += count[temp[i]] * r
            r += 1
      
           
        return c
        
        
        