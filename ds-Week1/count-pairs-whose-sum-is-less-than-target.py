class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] + nums[j] < target:
                    c += 1
        return c
        