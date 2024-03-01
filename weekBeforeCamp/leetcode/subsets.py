class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = [[]]
        currSet = []
        def backtrack(idx):
        
            if idx >= len(nums):
                return 
            
            for i in range(idx+1,len(nums)):
                currSet.append(nums[i])
                powerSet.append(currSet.copy())
                backtrack(i)
                currSet.pop()
        backtrack(-1)
        return powerSet


        