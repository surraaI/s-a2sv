class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        def inBound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        ans = [[0] * cols for _ in range(rows)]


        for r in range(rows):
            
            for c in range(cols):
                n = 0
                s = 0
                for rr in range(-1,2,1):
                    for cc in range(-1, 2):
                        if inBound(r + rr, c + cc):
                            s += img[r + rr][c + cc]
                            n += 1
                ans[r][c] = s//n

        return ans
        