class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res=0; i=0; j=0; ans={'T':0, 'F':0}
        while j<len(answerKey):
            while min(ans['T'], ans['F'])>k:
                ans[answerKey[i]]-=1
                i+=1
            ans[answerKey[j]]+=1
            j+=1
            if min(ans['T'], ans['F'])<=k:
                res=max(res, j-i)
            
        return res