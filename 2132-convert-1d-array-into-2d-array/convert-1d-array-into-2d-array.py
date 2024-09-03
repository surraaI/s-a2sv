class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        mat = []
        p = 0
        for i in range(m):
            t = []
            for j in range(n):
                t.append( original[p])
                p += 1
              
            mat.append(t)
                
        return mat

        