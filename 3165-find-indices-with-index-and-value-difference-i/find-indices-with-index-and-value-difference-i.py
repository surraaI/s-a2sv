class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        for i in range(n):
            for j in range(i + indexDifference, n):
                if abs(nums[j] - nums[i]) >= valueDifference:
                    return [i,j]

        return ans

        