class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = defaultdict(int)
        ans0 = []
        ans1 = []
        for game in matches:
            loses[game[1]] += 1
            if game[0] not in loses:
                loses[game[0]] = 0
  
        for p in loses:
            if loses[p] == 0:
                ans0.append(p)
            elif loses[p] == 1:
                ans1.append(p)
        ans0.sort()
        ans1.sort()
        return [ans0, ans1]

        

        
