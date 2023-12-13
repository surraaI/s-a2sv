class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p = nums.index(pivot)
        smaller = []
        greater = []
        p = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            elif nums[i]> pivot:
                greater.append(nums[i])
            else:
                p.append(nums[i])
        return smaller + p + greater

        
        
        
        print(nums)



        