class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        countT, window = {}, {}
        for i in t:
            countT[i] = 1+countT.get(i, 0)
        need , have = len(countT), 0
        res, resLen = [-1,-1], float('infinity')
        l = 0
        for j in range(len(s)):
            c = s[j]
            window[c] = 1+ window.get(c, 0)
            if c in countT and window[c] ==countT[c]:
                have += 1
            while have == need:
                if (j-l+1) < resLen:
                    res = [l,j]
                    resLen = j-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ''

            


        