"""

prefix tree implemenataion in detail

"""

class TrieNode:
    def __init__(self):
        self.children = []
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, val):
        node = self.root
        for ch in val:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True
        return node
    
    def search(self, val):
        node = self.root
        for ch in val:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end
    
    def startsWith(self.val):
        node = self.root
        for ch in val:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return True
