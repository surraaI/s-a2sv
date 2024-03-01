class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        nums = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = []
        def decode(ind, decoded):
            if ind >= len(digits):
                ans.append(''.join(decoded))
                return 

            for char in nums[digits[ind]]:
                decoded.append(char)
                decode(ind+1, decoded)
                decoded.pop()

        decode(0,[])
        return ans
        


