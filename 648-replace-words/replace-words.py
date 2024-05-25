
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    
    def search_shortest_root(self, word):
        current = self.root
        prefix = ""
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
            prefix += char
            if current.is_end_of_word:
                return prefix
        return None

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
       
        words = sentence.split()
        for i in range(len(words)):
            root = trie.search_shortest_root(words[i])
            if root:
                words[i] = root
        
        
        return ' '.join(words)
