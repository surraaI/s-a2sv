class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in cnt.items():
            buckets[freq].append(val)
        
        return list(chain(*buckets[::-1]))[:k]