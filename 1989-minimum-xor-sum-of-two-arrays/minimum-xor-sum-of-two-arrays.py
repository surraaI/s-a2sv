class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, used):
            if i >= n:
                return 0
            return min(((v ^ nums1[i]) + dp(i+1, used | (1 << j))) 
                        for j, v in enumerate(nums2) if (1 << j) & used == 0)
        n = len(nums2)
        return dp(0, 0)    