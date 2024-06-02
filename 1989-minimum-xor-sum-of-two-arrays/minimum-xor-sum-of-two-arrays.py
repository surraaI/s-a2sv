class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, used):
            if i >= n:
                return 0
            
            xor_sums = []
            for j, num in enumerate(nums2):
               
                if (1 << j) & used == 0:
                   
                    xor_sum = (num ^ nums1[i]) + dp(i + 1, used | (1 << j))
                    xor_sums.append(xor_sum)
            
            
            return min(xor_sums)
        
        n = len(nums2)  
        return dp(0, 0)  