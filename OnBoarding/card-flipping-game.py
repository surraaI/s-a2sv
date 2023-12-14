class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = float('inf')
        x = list(zip(fronts, backs))

        
        left = [i[0] for i in x if len(set(i)) < 2]
        print(left,fronts,backs)
        for i in left:
            fronts = list(filter(lambda a: a != i, fronts))
            backs = list(filter(lambda a: a != i, backs))
        
        print(fronts, backs)
        # y = [i for i in x if len(set(i))>=2 and i[0] not in left and i[1] not in left ]
        # print(y)
        # z = [min(j) for j in y]
        return min(fronts+backs) if fronts+backs else 0
        
        