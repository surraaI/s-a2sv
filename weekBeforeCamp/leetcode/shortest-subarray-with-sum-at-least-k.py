class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        cumSum = [0]
        for n in nums:
            cumSum.append(cumSum[-1]+n)
            
        monoQ = collections.deque()
        ans = len(nums)+1
        for x, sumX in enumerate(cumSum):
            while monoQ and sumX <= cumSum[monoQ[-1]]:
                monoQ.pop()
            
            while monoQ and sumX - cumSum[monoQ[0]] >= k:
                ans = min(ans, x - monoQ.popleft())
            
            monoQ.append(x)
        return ans if (ans < len(nums) + 1) else -1
        