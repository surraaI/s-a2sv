class Solution:
    def maxScore(self, s: str) -> int:
        cur_sum = s.count('1')
        m = 0
      
        for i in range(len(s)-1):
            if s[i] == '1':
                cur_sum -= 1
            else:
                cur_sum += 1
            m = max(m, cur_sum)
        return m
        