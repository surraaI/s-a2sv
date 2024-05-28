class Solution:
    def findMaximumXOR(self, nums):    
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1): 
            mask |= (1 << i)
            found_prefixes = set()
            
            for num in nums:
                found_prefixes.add(num & mask)
            
            temp = max_xor | (1 << i)
            for prefix in found_prefixes:
                if (prefix ^ temp) in found_prefixes:
                    max_xor = temp
                    break
        
        return max_xor

