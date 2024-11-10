import random
import bisect

class Solution:
    def __init__(self, w: list[int]):
        # Compute prefix sum
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        # Get a random number from 1 to total_sum (since 0 <= random() < 1, multiplying it by total_sum gives range [0, total_sum))
        target = random.randint(1, self.total_sum)
        # Binary search to find the correct index based on the prefix sums
        return bisect.bisect_left(self.prefix_sums, target)
