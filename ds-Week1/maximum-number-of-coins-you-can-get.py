class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        i = 0
        l = len(piles)-1
        rl = l - 1
        s = 0 
        while i < rl:
            s += piles[rl]
            i+= 1
            l -= 2
            rl = l-1

        return s
