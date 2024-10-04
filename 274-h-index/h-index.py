class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        prefix = [0] * len(citations)
        prefix[0] = 1

        if len(citations) == 1:
            if citations[0] > 0:
                return 1

        for i in range(1,len(citations)):
            prefix[i] = 1 + prefix[i-1]
    
        m = 0
        for i in range(len(citations)):
            if citations[i] >= prefix[i]:
                m = max(m, prefix[i])

        return m
       
        