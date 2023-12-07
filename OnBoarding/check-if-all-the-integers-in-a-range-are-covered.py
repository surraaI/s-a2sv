class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = []
        ranges = sorted(ranges)
        

        for i in range(left, right+1):
            for j in ranges:
                if i>= j[0] and i <= j[1]:
                    ans.append(True)
                    break
        return len(ans) == (right - left +1)
                
            

           