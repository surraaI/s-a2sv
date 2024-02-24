class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        index = collections.deque(range(n))
        ans = [None] * (n)
        
        for card in range(len(deck)):
            
            ans[index.popleft()] = deck[card]
            if index:
                index.append(index.popleft())
        return ans
       