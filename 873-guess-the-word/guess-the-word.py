# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
        
        def match(w, x):
            c = 0
            for i in range(6):
                if w[i] == x[i]:
                    c += 1
            return c

        while len(words) > 0:
            curr_word = random.choice(words)
            m = master.guess(curr_word)
            
            if m == 6:
                return curr_word
            words = [w for w in words if match(w, curr_word) == m]

        return 
            


            


        