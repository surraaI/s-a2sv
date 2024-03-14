class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(mid):
            days = 1
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    days += 1
                    cur = weight
                else:
                    cur += weight
            return days
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = low + (high-low)//2
            if checker(mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
