class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.sum = collections.defaultdict(int)

    def add_and_merge(self, i: int, num: int) -> int:
        self.sum[i] = num
        if i - 1 in self.sum:
            self.union(i - 1, i)

        if i + 1 in self.sum: 
            self.union(i, i + 1)

        parenti = self.find(i)
        return self.sum[parenti]

    def find(self, x: int) -> int:
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:

        parentx, parenty = self.find(x), self.find(y)
        if parentx == parenty: 
            return
        if self.rank[parentx] > self.rank[parenty]: 
            self.parent[parenty] = parentx
            self.sum[parentx] += self.sum[parenty]
            
        elif self.rank[parentx] < self.rank[parenty]: 
            self.parent[parentx] = parenty
            self.sum[parenty] += self.sum[parentx]
        else:
            self.parent[parenty] = parentx
            self.rank[parentx] += 1
            self.sum[parentx] += self.sum[parenty]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        res = [0 for _ in range(n)]
        max_sum_segment = 0
        for i in range(n - 1, -1, -1):
            res[i] = max_sum_segment
            q = removeQueries[i]
            max_sum_segment = max(max_sum_segment, uf.add_and_merge(q, nums[q]))
        return res