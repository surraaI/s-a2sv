class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[i] = 0
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    d[i] = d.get(i,0) + 1     
        return list(d.values())