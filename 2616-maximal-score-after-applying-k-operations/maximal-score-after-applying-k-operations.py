class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        score = 0
        for i in range(k):
            curr = heapq.heappop(heap)
            score += -1 * curr
            heapq.heappush(heap,-1 *  math.ceil(-curr/3))
        
        return score 


        