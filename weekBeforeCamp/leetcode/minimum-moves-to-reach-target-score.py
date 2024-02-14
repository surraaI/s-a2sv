class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0
        
        while maxDoubles and target>1:
            if target%2 == 0:
                    op += 1
                    target /= 2
                    maxDoubles -= 1
            else:
                    target -= 1
                    op += 1
            
       
        op += int(target-1)
        return op
