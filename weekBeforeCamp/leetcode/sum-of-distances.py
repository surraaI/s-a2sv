class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ind = defaultdict(list)
        for i in range(len(nums)):
            ind[nums[i]].append(i)
        arr=[0] * len(nums)
        for num, indices in ind.items():
            suffixSum = sum(indices)
            preffixSum = 0
            s = len(indices)
            p = 0
            for i in indices:
                preffixSum += i
                p += 1
                suffixSum -= i
                s -= 1
                arr[i] = -preffixSum + p*i - s*i + suffixSum
            
            
        return arr

             




        