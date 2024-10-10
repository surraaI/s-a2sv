class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        prev = [float('inf')] * n
        curr = [float('inf')] * n
       
        prev[k-1] = 0
        curr[k-1] = 0

        for i in range(1,n):
            for u, v, w in times:
                curr[v-1] = min(curr[v-1], prev[u-1] + w)

            prev = curr[:]

        
        res = max(curr)

        return res if res != float('inf') else -1

        