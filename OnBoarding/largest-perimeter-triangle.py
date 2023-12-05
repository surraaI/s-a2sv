class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        lp = 0
        nums = sorted(nums)
        j = 0
        while j < len(nums)-2:
            if nums[j] +nums[j+1] > nums[j+2]:
                lp = max(lp, nums[j]+nums[j+1] +nums[j+2])
            j += 1
        
                
             
        return lp