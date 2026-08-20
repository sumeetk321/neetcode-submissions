class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        def dfs(i, j, word):
            print(word, i, j)
            if word=="":
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j]:
                return False
            if board[i][j]==word[0]:
                visited[i][j] = True
                out = dfs(i+1, j, word[1:]) or dfs(i-1, j, word[1:]) or dfs(i, j-1, word[1:]) or dfs(i, j+1, word[1:])
                visited[i][j] = False
                return out
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
        return False