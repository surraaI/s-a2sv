class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def bt(ind, curr, currSum):
            if currSum == target:
                ans.append(curr.copy())
                return
            if ind >= len(candidates) or currSum > target:
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                bt(i+1, curr, currSum + candidates[i])
                curr.pop()
                i += 1
        bt(0, [],0)
        return ans


            