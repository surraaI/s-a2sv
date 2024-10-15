class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        for i in range(rows):
            grid[i].sort()

        @cache
        def f(mask, M):
            if mask == 0:
                return 0
            ans = 0
            candidates = []
            for i in range(rows):
                if mask & (1 << i):
                    j = bisect.bisect_right(grid[i], M) - 1
                    if j >= 0:
                        candidates.append((grid[i][j], i))
            if not candidates:
                return 0
            maximumValue = max(candidates)[0]
            for v, i in candidates:
                if v != maximumValue:
                    continue
                ans = max(ans, f(mask - (1 << i), v - 1) + v)
            return ans

        ans = f((1 << rows) - 1, 100)
        return ans