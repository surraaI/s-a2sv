class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            ans[i] = ans[i-1] + nums[i-1]
        return ans[1:]