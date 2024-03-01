class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        validParenthesis = []
        def backtrack(openP, closeP, validParenthesis):
            if closeP == n and openP == n:
                ans.append(''.join(validParenthesis.copy()))
                return
            if openP < n:
                validParenthesis.append('(')
                backtrack(openP+1, closeP,validParenthesis)
                validParenthesis.pop()
            if closeP < openP:
                validParenthesis.append(')')
                backtrack(openP, closeP+1, validParenthesis)
                validParenthesis.pop()
        backtrack(0, 0, validParenthesis)
        return ans