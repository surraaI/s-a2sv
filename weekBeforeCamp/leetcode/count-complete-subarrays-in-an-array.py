class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        l = r = 0
        distnict = len(set(nums))
        currDistnict = {}
        currCount = 0
        c = 0
        while r < len(nums):
            if nums[r] in currDistnict:
                currDistnict[nums[r]] +=  1
            else:
                currDistnict[nums[r]] = 1
                currCount += 1
            if currCount == distnict:
                while l <= r and currCount == distnict:
                    c += len(nums) - r
                    currDistnict[nums[l]] -= 1
                    if  currDistnict[nums[l]] == 0:
                        currCount -= 1
                        del  currDistnict[nums[l]]
                    l += 1
            r += 1
        return c

            


        