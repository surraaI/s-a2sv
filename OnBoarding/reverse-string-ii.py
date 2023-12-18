class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # j =0
        # for i in range(len(s)-2*k+1):
        #     s = s[j:j+k][::-1] +s[j+k:]
        #     j += 2*k
        # return s

        j= 0
        ans = ''
        while j < len(s):
            s = s[:j]+s[j:j+k][::-1] +s[j+k:]
            j += 2*k
        return s
            
        