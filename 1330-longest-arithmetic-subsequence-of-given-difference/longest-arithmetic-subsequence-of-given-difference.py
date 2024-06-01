class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 0

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
            max_length = max(max_length, dp[num])

        return max_length


            