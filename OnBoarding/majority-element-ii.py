class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums.count(i)>(len(nums)/3) and i not in ans:
                ans.append(i)
        return ans