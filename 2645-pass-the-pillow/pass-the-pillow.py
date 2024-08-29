class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = 0
        dir = 1
        while time:
            if dir == 1:
                p += 1
                if p == n-1:
                    dir = -1
            else:
                p -= 1
                if p == 0:
                    dir = 1
            time -= 1
        
        return p + 1
            


        
        
        