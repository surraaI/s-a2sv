class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
    
        
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        
        for r in range(1, k):
            if r == k - r:  
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        
        return remainder_count[0] % 2 == 0
                

            