class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[i] = n
        s= 0
        for i in range(len(d)):
            if d[i] %2 == 0:
                s += d[i]
        
        ans = []
        for i in range(len(queries)):
            temp = d[queries[i][1]]
            if temp%2 == 0 and queries[i][0] %2 ==0:
                s += queries[i][0]
                d[queries[i][1]] += queries[i][0]
            elif temp %2 == 0 and queries[i][0] %2 != 0:
                s -= temp
                d[queries[i][1]] += queries[i][0]
            elif temp %2 !=0 and queries[i][0] %2 != 0:

                d[queries[i][1]] += queries[i][0]
                s += d[queries[i][1]]
            elif temp %2 !=0 and queries[i][0] %2 == 0:
                d[queries[i][1]] += queries[i][0]
            
            


            
            ans.append(s)
            
        return ans
