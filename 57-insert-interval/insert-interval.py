class Solution:
    def insert(self, i: List[List[int]], n: List[int]) -> List[List[int]]:
        return (r:=[],any(setitem(r[-1],1,max(r[-1][1],e)) if r and r[-1][1]>=s else r.append([s,e]) for s,e in sorted(i+[n])))[0]