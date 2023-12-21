class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows= len(strs)
        cols = len(strs[0])
        arr = []
        for c in range(cols):
            t = []
            for r in range(rows):
                t.append(strs[r][c])
            arr.append(t)
        c= 0
       
        for j in arr:
            if j != sorted(j):
                c += 1
            
        return c