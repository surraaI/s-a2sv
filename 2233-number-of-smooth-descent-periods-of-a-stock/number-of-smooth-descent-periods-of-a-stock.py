class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = r = 0
        ans = 0
        while l < len(prices):
            while r < len(prices) - 1 and prices[r] - prices[r+1] == 1:
                r += 1

            ans += (r - l + 1) * (r - l + 2) // 2

            r += 1
            l = r
        return ans
