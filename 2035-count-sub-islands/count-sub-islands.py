class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            
            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True 
            
            
            grid2[r][c] = 0
            
            
            is_sub_island = True
            
            if grid1[r][c] == 0:
                is_sub_island = False
            
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if not dfs(r + dr, c + dc):
                    is_sub_island = False
            
            return is_sub_island
        
        
        sub_island_count = 0
        
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:  
                    if dfs(r, c):  
                        sub_island_count += 1
        
        return sub_island_count