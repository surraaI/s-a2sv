class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                return False
            current = current.children[index]
        return True if current.is_end else False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                return False
            current = current.children[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)