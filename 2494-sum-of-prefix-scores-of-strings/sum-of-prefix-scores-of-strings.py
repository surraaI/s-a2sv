class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.frequency += 1
    def search(self, word):
        curr = self.root
        c = 0
        for ch in word:
            curr = curr.children[ch]
            c += curr.frequency
        return c
    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = [0] * len(words)
        trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(len(words)):
            ans[i] = trie.search(words[i])
            
        return ans


        