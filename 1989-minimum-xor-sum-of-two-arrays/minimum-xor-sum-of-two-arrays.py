class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        inf = 10 ** 10

        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 0
            
            best = inf
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    best = min(best, dp(i+1, mask | (1 << j)) + (nums2[j] ^ nums1[i]))

            return best

        return dp(0,0)