class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        ind = {}
        for i in range(len(tickets)):
            ind[i] = tickets[i]
        ticket = 0
       
        while ind[k] > 0:
            for i in ind:
                if ind[i] > 0:
                    ind[i] -= 1
                    ticket += 1
                if ind[k] == 0:
                    break
            
        return ticket

            
