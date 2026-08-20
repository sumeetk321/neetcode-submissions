class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        tmp = self.root
        for c in word:
            idx = ord(c)-97
            if not tmp.children[idx]:
                tmp.children[idx] = Node()
            tmp = tmp.children[idx]

        tmp.isWord = True


    def search(self, word: str) -> bool:
        q = collections.deque()
        q.append((0, self.root))
        while q:
            i, pop = q.pop()
            if not pop:
                continue
            if i==len(word):
                if pop.isWord:
                    return True
                continue
            newc = word[i]
            idx = ord(newc)-97
            if newc=='.':
                q.extend((i+1, child) for child in pop.children)
            else:
                q.append((i+1, pop.children[idx]))

        return False
                

                
            
