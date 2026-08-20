class Node:
    def __init__(self):
        self.children = [None] * 26 
        self.prefix = ""
        self.isWord = False
    def addChild(self, idx, val):
        self.children[idx] = val
        val.prefix = self.prefix+chr(idx+97)

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.children[ord(ch.lower())-97]:
                curr.addChild(ord(ch.lower())-97, Node())

            curr = curr.children[ord(ch.lower())-97]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if not curr.children[ord(ch.lower())-97]:
                return False
            curr = curr.children[ord(ch.lower())-97]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not curr.children[ord(ch.lower())-97]:
                return False
            curr = curr.children[ord(ch.lower())-97]

        return curr!=None
        
        