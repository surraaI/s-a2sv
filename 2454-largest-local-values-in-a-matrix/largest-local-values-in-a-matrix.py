class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for _ in range(n-2)]  # Initialize ans with proper dimensions

        for i in range(n - 2):
            for j in range(n - 2):
                # Calculate the maximum value in the 3x3 sub-grid starting at (i, j)
                max_val = max(grid[i + ii][j + jj] for ii in range(3) for jj in range(3))
                ans[i][j] = max_val  # Assign the maximum value directly
        
        return ans
