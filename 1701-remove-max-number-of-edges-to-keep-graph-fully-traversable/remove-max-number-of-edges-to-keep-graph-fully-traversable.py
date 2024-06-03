class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n
    
    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]: # py to px
            self.par[py] = px
            self.rank[px] += self.rank[py]
        else: # px to py
            self.par[px] = py
            self.rank[py] += self.rank[px]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        import collections
        type2edge = collections.defaultdict(list)
        for ty, u, v in edges:
            type2edge[ty].append([u, v])
        
        ans = 0

        # alice
        dsua = DSU(n+1)
        for u, v in type2edge[3]: # join common
            if dsua.find(u) == dsua.find(v):
                ans += 1
            else:
                dsua.union(u, v)
        for u, v in type2edge[1]:
            if dsua.find(u) == dsua.find(v):
                ans += 1
            else:
                dsua.union(u, v)
        
        for i in range(n):
            dsua.find(i)
        if len(set(dsua.par[1:])) > 1: # diff groups
            return -1
        
        # bob
        dsub = DSU(n+1)
        for u, v in type2edge[3]:
            if dsub.find(u) != dsub.find(v):
                dsub.union(u, v)
        for u, v in type2edge[2]:
            if dsub.find(u) == dsub.find(v):
                ans += 1
            else:
                dsub.union(u, v)
        
        for i in range(n):
            dsub.find(i)
        if len(set(dsub.par[1:])) > 1:
            return -1
        
        return ans