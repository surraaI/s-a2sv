class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(k):
            h = 0
            for i in  piles:
                if i%k == 0:
                    h += i/k
                else:
                    h += (i//k)+1
              
            return h
    
        l = 1
        r = max(piles)
        minimumk = float('inf')
        while l <= r:
            mid = l + (r-l)//2
            if checker(mid) > h:
                l = mid + 1 
            else:
                minimumk = min(minimumk, mid)
                r = mid -1
        
        return minimumk



        