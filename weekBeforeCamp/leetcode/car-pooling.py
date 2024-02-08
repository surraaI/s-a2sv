class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for i in trips:
            n = max(n, i[-1])
        arr = [0] * (n)
        for passengers, start, end in trips:
            arr[start] += passengers
            if end < n:
                arr[end] -= passengers
            
        prefix_sum = [0]* (n+1)
        
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
            if prefix_sum[i] > capacity:
                
                return False
        return True

        