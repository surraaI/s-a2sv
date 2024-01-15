class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = 0
        
        for i in range(k):
            
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'o' or s[i] == 'u' or s[i] == 'i':
                c += 1
        print(c)
        m = c
        l = 0
     
        for i in range(k, len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'o' or s[i] == 'u' or s[i] == 'i':
                c += 1
            if s[l] == 'a' or s[l] == 'e' or s[l] == 'o' or s[l] == 'u' or s[l] == 'i':
                c -= 1
            l += 1
            
            m = max(m, c)
            print(i, m, c)
            


            
            
        return m