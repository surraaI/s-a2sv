class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if abs(x)==x]
        neg = [x for x in nums if abs(x)!=x]
        ans = []
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
        