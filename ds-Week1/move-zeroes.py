class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker = 0
        place = 0
        while place < len(nums):
            if nums[place] == 0:
                while seeker < len(nums) and nums[seeker] == 0:
                    seeker += 1
                if seeker < len(nums):
                    nums[seeker], nums[place] = nums[place], nums[seeker]
                

                place += 1
            else:
                place += 1
                seeker += 1
            
        
            
            