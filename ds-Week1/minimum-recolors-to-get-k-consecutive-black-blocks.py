class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        minimum = float('inf')

        while i < len(blocks)-k+1:
            j = i + k 
            l = i
            countW = 0
            while l < j:
                if blocks[l] == 'W':
                    countW += 1
                l += 1
            minimum = min(minimum, countW)
            i += 1
        return minimum
            

