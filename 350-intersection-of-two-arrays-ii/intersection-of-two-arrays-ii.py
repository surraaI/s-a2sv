class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = {} 
        d ={}
        ans = []
        for i in nums1:
           c[i] = c.get(i,0) + 1
        for j in nums2:
            d[j] = d.get(j,0) + 1
        for j in d:
            if j in c:
                ans += [j] * min(c[j] , d[j])
        return ans


        