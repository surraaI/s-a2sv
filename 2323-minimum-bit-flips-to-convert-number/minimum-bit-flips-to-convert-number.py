class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b1 = bin(start)[2:]
        b2 = bin(goal)[2:]
        
        c = 0
        b1 = '0' * (32 - len(b1)) + b1
        b2 = '0' * (32 - len(b2)) + b2
        

        for i in range(32):
            if b1[i] != b2[i]:
                c += 1
        return c
        