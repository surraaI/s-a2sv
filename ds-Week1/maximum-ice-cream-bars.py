class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = max(costs)
        count = [0]* (mx+1)
        ans = 0
        for i in range(len(costs)):
            count[costs[i]] += 1
        arr = []
        for i in range(len(count)):
            arr.extend([i] * count[i])
        s = 0
        c =0
        for i in range(len(arr)):
            if s + arr[i] <= coins:
                s += arr[i]
                c += 1
        return c

        