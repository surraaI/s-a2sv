class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        currentNums = []
        ans = []
        currSum = 0

        def backtrack(idx, currSum, currentnums):
            if idx >= len(candidates):
                return
            if currSum > target:
                    return
                
            for i in range(idx,len(candidates)):
                currentNums.append(candidates[i])
                currSum += candidates[i]
                if currSum == target:
                    ans.append(currentNums.copy()) 
                
                backtrack(i,currSum, currentNums)
                currentNums.pop()
                currSum -= candidates[i]
        backtrack(0,currSum, currentNums)
        return ans
        
