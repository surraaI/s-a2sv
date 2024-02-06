class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ind = defaultdict(list)
        for i in range(len(cards)):
            ind[cards[i]].append(i)
        m = float('inf')
        for j in cards:
            if len(ind[j]) >= 2:
                for i in range(len(ind[j])-1):
                    
                    m = min(m, ind[j][i+1] - ind[j][i] + 1)
                   
       
        return m if m != float('inf') else -1
        