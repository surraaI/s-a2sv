class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def bt(num,currNums, currSum):
            if num > 9 or currSum > n:
                return
            if currSum == n and len(currNums) == k:
                ans.append(currNums.copy())
            for i in range(num+1, 10):
                currNums.append(i)
                currSum += i
                bt(i,currNums, currSum)
                currNums.pop()
                currSum -= i
        ans = []
        currNums = []
        bt(0,currNums,0)
        return ans
        
