class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        Mask = (1<<n) - 1
        ans = []

        def backtrack(mask, cur):
            if mask == Mask:
                if cur not in ans:
                    ans.append(cur[:]) 
                return
            for i in range(n):
                if mask & (1<<i) == 0:
                    cur.append(nums[i])
                    backtrack(mask | (1<<i), cur[:]) 
                    cur.pop()

        cur = []
        backtrack(0, cur)
        return ans