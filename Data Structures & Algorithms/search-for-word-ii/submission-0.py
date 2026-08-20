class Node:

    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False
        self.word = ""

class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for w in word:
            curr = curr.children[w]
        curr.is_word = True
        curr.word = word
    
    # def search(self, word):
    #     curr = self.root
    #     for w in word:
    #         if w not in curr.children:
    #             return False
    #         curr = curr.children[w]
    #     return curr.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        t = Trie()
        for w in words:
            t.insert(w)
        wordsFound = set()
        def dfs(i, j, tpointer, visited):
            if (i, j) in visited or i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] not in tpointer.children:
                return
            visited.add((i, j))
            tpointer = tpointer.children[board[i][j]]
            if tpointer.is_word:
                wordsFound.add(tpointer.word)
                res = True
            dfs(i-1, j, tpointer, visited)
            dfs(i+1, j, tpointer, visited)
            dfs(i, j-1, tpointer, visited)
            dfs(i, j+1, tpointer, visited)
            visited.remove((i, j))
            return
        
        for i in range(m):
            for j in range(n):
                curr = t.root
                dfs(i, j, curr, set())
        return list(wordsFound)



        