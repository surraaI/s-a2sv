class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = mean * (n + len(rolls))

        rem = s - sum(rolls)

        ans = []
        c = rem//n
        if c > 6 or c <= 0:
            return []

        if rem % n == 0:
            for i in range(n):
                ans.append(c)
        else:
            
            for i in range(n):
                ans.append(c)
            r = rem % n
            for i in range(n):
                if r:
                    ans[i] += 1
                    if ans[i] > 6:
                        return []
                else:
                    break
                r -= 1

            
            
        
        return ans 