class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows-2):
            for c in range(cols-2):
                s = sum(grid[r][c:c+3]) + grid[r+1][c+1] + sum(grid[r+2][c:c+3])
                m = max(m,s)


        return m


        