class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        m = 0
        ans = 0
        for i in range(len(flips)):
            m = max(m, flips[i])
            if i+1 >= m:
                ans += 1
        return ans
