class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for i in range(cols)] for j in range(rows)]

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            while q:
                r, c = q.popleft()
                if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                    continue
                if grid[r][c]=="1":
                    visited[r][c] = True
                    q.append((r+1, c))
                    q.append((r-1, c))
                    q.append((r, c+1))
                    q.append((r, c-1))

        res = 0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c]=="1":
                    bfs(r, c)
                    res+=1
        return res