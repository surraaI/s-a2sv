class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        def groupify(w):
            groups = []
            i = 0
            n = len(w)

            while i < n:
                curr = w[i]
                j =i
                while j < n and w[j] == curr:
                    j += 1
                groups.append((curr, j - i))
                i = j
            return groups
        
        g = groupify(s)
        for w in words:
            curr = groupify(w)
            if len(curr) != len(g):
                continue
            
            flag = True
            for j in range(len(curr)):
                if g[j][0] != curr[j][0]:
                    flag = False
                    continue
                if g[j][1] <= 2:
                    if curr[j][1] != g[j][1]:
                        flag = False
                elif g[j][0] == curr[j][0] and g[j][1] < curr[j][1]:
                    flag = False
                
            if flag:
                ans += 1

        return ans
                
                 


        return 0

