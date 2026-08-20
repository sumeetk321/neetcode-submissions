class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        def bfs(r, c):
            oset = set()
            q = collections.deque()
            q.append((r, c))
            surrounded = True
            while q:
                i, j = q.popleft()
                if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited:
                    continue
                visited.add((i, j))
                if board[i][j]=="O":
                    oset.add((i, j))
                    if not (i-1>=0 and i+1 < rows and j-1 >= 0 and j+1 < cols):
                        surrounded = False
                    
                    q.extend(((i-1, j), (i+1, j), (i, j-1), (i, j+1)))

            if surrounded:
                for m, n in oset:
                    board[m][n] = "X"

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O" and (i, j) not in visited:
                    bfs(i, j)

        

