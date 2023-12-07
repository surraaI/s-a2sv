class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        print(nums)
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                return i
        