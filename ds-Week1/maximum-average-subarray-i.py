class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = sum(nums[:k])
        i = 0
        j = k
        s = sum(nums[:k])
        while j < len(nums):
            s += nums[j] - nums[i]
            m = max(m, s)
            i += 1
            j += 1
        return m/k