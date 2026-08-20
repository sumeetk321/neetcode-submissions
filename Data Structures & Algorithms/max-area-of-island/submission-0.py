class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            count = 0
            while q:
                r, c = q.popleft()
                if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                    continue
                if grid[r][c]==1:
                    count+=1
                    visited[r][c] = True
                    q.extend([(r+1, c), (r-1, c), (r, c+1), (r, c-1)])

            return count
        res = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j]:
                    continue
                if grid[i][j]==1:
                    res = max(res, bfs(i, j))
        return res
        