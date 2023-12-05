class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
           
            for j in range(nums[i]):
                ans.append(nums[i+1])
            i += 2
        return ans