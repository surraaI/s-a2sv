class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            for col in range(cols):
                d[col+row].append(mat[row][col])
        ans = []
        print(d)
        for i in range(len(d)):
            if i%2 == 0:
                ans += d[i][::-1]
            else:
                ans += d[i]
        return ans
   
