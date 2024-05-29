class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def check(self, word):
        curr = self.root
        for ch in word:
            curr = curr.children.get(ch)
            if not curr or not curr.is_end:
                return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        longest = ''
        trie = Trie()
        
        
        words.sort()
        
       
        for word in words:
            trie.insert(word)
        
       
        for word in words:
            if trie.check(word):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        
        return longest
