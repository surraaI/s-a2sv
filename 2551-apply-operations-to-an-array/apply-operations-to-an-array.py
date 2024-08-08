class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0
        w = 0
        
        while w < n:
            if nums[w] == 0:
                r = w
                while  r < n:
                    if nums[r] != 0:
                        nums[w], nums[r] = nums[r], nums[w]
                        break
                    r += 1
            w += 1


        return nums

        