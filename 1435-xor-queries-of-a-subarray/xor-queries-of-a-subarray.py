class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        
        
        result = []
        for left, right in queries:
            if left == 0:
                result.append(prefix[right])
            else:
                result.append(prefix[right] ^ prefix[left - 1])
        
        return result