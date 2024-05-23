class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26  

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end = True
        
    def search(self, word: str) -> bool:
        return self._search_in_node(word, 0, self.root)
    
    def _search_in_node(self, word: str, index: int, node: TrieNode) -> bool:
        current = node
        
        for i in range(index, len(word)):
            char = word[i]
            if char == '.':
                
                for child in current.children:
                    if child and self._search_in_node(word, i + 1, child):
                        return True
                return False
            else:
                
                idx = ord(char) - ord('a')
                if not current.children[idx]:
                    return False
                current = current.children[idx]
        
        return current.is_end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
