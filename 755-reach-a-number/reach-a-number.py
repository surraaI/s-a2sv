class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)  
        n = 0
        sum_steps = 0
        
        while sum_steps < target or (sum_steps - target) % 2 != 0:
            n += 1
            sum_steps += n
            
        return n