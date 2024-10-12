class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))


        heap = [[start_node,-1]]
        chances = {i:0 for i in range(n)}
        chances[start_node] = 1

        while heap:
            curr, prob = heapq.heappop(heap)
            prob *= -1

            for child, cprob in graph[curr]:
                if prob * cprob > chances[child]:
                    chances[child] = prob * cprob
                    heapq.heappush(heap, (child, -chances[child]))
      
        return chances[end_node]
