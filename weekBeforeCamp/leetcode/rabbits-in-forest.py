class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mp = {}
        for i in answers:
            mp[i]  = mp.get(i,0) + 1
        ans = 0
        for i in mp:
            t = ceil(mp[i]/(i+1))
            ans += (t*(i+1))
            
        return ans
        