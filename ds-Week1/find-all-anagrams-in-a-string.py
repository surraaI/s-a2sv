class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pArr = [0] * 26
        sArr = [0] * 26
        l = 0
        k = len(p)
        ans= []
        for i in p:
            pArr[ord(i)-97] += 1
        for i in range(len(s)):
            sArr[ord(s[i])-97] += 1
            if i - l + 1 == k:
                if pArr == sArr:
                    ans.append(l)
                sArr[ord(s[l])-97] -= 1
                l += 1
        return ans
                
            
                
        