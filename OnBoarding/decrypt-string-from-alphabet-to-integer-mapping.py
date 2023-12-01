class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {}
        i = 'a'
        j = 1
        
 

        while True:
            d[str(j)] = chr(ord(i))
            i = chr(ord(i) + 1)
            if i > 'z':
                break
            j = int(j) +1
        print(d)
        cur =0
        ans = ''
        while cur < len(s)-2:
            if s[cur+2] == '#':
                ans += d[s[cur:cur+2]]
                cur += 3
            else:
                ans += d[s[cur]]
                cur += 1
        while cur < len(s):
            ans += d[s[cur]]
            cur += 1
        return ans
       
            

    
        