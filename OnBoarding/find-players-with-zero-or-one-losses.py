class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        win = {}
        lose = {}
        for i in matches:
            win[i[0]] = win.get(i[0], 0) +1
            lose[i[1]] = lose.get(i[1],0) + 1
        ans[0] = sorted(set(win.keys()) - set(lose.keys()))
        ans[1] = sorted([key for key in lose if lose[key] == 1])
       
        return ans
        