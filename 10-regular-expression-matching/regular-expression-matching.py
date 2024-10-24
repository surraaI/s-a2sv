class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
        # Base case: empty string and empty pattern match
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c*, etc. where they can match an empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Match current character or '.'
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Match zero occurrences of the element before '*'
                    dp[i][j] = dp[i][j - 2]
                    # Match one or more occurrences of the element before '*'
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[len(s)][len(p)]
            