class Trie:
    def __init__(self):
        self.data = [None, None]
    

    def add(self, val):
        node = self.data
        for  i  in range(31,-1,-1):
            bit = val >> i & 1

            if node[bit]  is None:
                node[bit] = [None, None] 
            node = node[bit]
        
        
    def maxXor(self, val):
        node = self.data
        res  = 0
        for  i  in range(31,-1,-1):
            bit = val >> i & 1
            if node[not bit]  is not None:
                node = node[not bit]
                res |= 1 << i
            else:
                node = node[bit]
            

        return res
            



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans =  0 
        trie = Trie()

        trie.add(nums[0])
        for i, num in enumerate(nums):
            if i > 0:
                ans = max(ans, trie.maxXor(num))
                trie.add(num)           

        return ans
        