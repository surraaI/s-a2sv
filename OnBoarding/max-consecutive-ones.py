class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                count +=1
                maxCount = max(maxCount, count)
            else:
                maxCount = max(maxCount, count)
                count = 0
            i += 1
        return maxCount