class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * (n+1)
        arr = [0] * (n)
        
        
        for a, b , c in bookings:
            arr[a-1] += c
            if  b < n:
                arr[b] -= c
        
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
        return prefix_sum[1:]
