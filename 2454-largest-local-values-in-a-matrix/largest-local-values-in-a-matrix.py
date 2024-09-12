class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[] for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                m = 0
                for ii in range(3):
                    for jj in range(3):
                        m = max(m, grid[i + ii][j + jj])
                    

                ans[i].append(m)

        return ans


        