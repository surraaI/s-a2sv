class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(num):
            if len(path)==k:
                ans.append(path.copy())
                return
            for next_candidate in range(num+1, n+1):
                path.append(next_candidate)
                backtrack(next_candidate)
                path.pop()
        backtrack(0)
        return ans