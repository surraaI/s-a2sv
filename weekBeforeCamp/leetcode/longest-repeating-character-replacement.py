class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        mx=0

        start=0
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            windowlen = end-start+1
            maxcount = max(count.values())
            if (windowlen - maxcount) > k:
                count[s[start]]-=1
                start+=1
            mx=max(mx, end-start+1)
        return mx  