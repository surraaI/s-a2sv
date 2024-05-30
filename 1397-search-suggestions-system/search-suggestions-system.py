from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''
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
        curr.word = word
        curr.is_end = True

    def generateSuggestion(self, prefix):
        ans = []
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]

        self._dfs(curr, ans)
        
        ans.sort()
        return ans[:3] if len(ans) >= 3 else ans

    def _dfs(self, node, result):
        if node.is_end:
            result.append(node.word)
        for child in node.children.values():
            self._dfs(child, result)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
      
        for word in products:
            trie.insert(word)
        
        ans = []
        for i in range(1, len(searchWord) + 1):
            ans.append(trie.generateSuggestion(searchWord[:i]))
        
        return ans
