class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        rest = []
        
        for i, query in enumerate(queries):
            a, b = sorted(query)
            if a == b or heights[b] > heights[a]:
                res[i] = b
            else:
                rest.append((i, a, b))
        
        rest.sort(key=lambda x: x[2], reverse=True)
        monostack = deque()
        currInd = len(heights) - 1

        for i, a, b in rest:
            while currInd >= b:
                while monostack and heights[currInd] >= heights[monostack[0]]:
                    monostack.popleft()
                monostack.appendleft(currInd)
                currInd -= 1

            loc = -1
            l, r = 0, len(monostack) - 1
            while l <= r:
                p = (l + r) // 2
                if heights[monostack[p]] > heights[a]:
                    loc = monostack[p]
                    r = p - 1
                else:
                    l = p + 1
            res[i] = loc
        
        return res
