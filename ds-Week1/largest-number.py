class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums)):
            
            for j in range(1, len(nums)-i):
                first = nums[j] + nums[j-1]
                sec = nums[j-1] + nums[j]
                if first > sec:
                    nums[j] , nums[j-1] = nums[j-1], nums[j]
        
        if nums[0] == '0':
            return '0'

        return ''.join(nums)
