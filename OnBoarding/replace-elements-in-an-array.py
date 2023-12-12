class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        
        
        for i in range(len(nums)):
            d[nums[i]] = i
        for j in range(len(operations)):
            d[operations[j][1]] = d[operations[j][0]]
            del d[operations[j][0]]
       
        k = dict(sorted(d.items(),key= lambda x:x[1]))
        ans = []
        

        for i in k.keys():
            ans.append(i)
        return ans


        

        