class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = 0
        n = len(costs)
        # -10 -170 350 10 A  -170 -10 10 350
        # 10 170 -350 -10 B   -350 -10 10 170
        diffA = {}
        diffB = {}
        arrA = []
        arrB = []
        for i in range(n):
            diff = costs[i][0] - costs[i][1]
            diffA[i] = diff
        for i in range(n):
            diff = costs[i][1] - costs[i][0]
            diffB[i] = diff
        sortedA = dict(sorted(diffA.items(),key=lambda item:item[1]))
        sortedB = dict(sorted(diffA.items(),key=lambda item:item[1]))
        lstA = list(sortedA.keys())
        lstB = list(sortedB.keys())
        visited = []
        for i in range(n//2):
            s+= costs[lstA[i]][0]
            visited.append(lstA[i])
        for i in range(n):
            if lstB[i] not in visited:
                s+= costs[lstB[i]][1]
      
        return s



        


        