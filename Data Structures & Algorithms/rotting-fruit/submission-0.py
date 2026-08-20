class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fruits = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    fruits.add((i, j))
        visited = set()
        def bfs(q):
            out = 0
            while q:
                time, i, j = q.popleft()
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j]==0:
                    continue
                out = max(out, time)
                visited.add((i,j))
                q.extend(((time+1, i+1, j), (time+1, i-1, j), (time+1, i, j-1), (time+1, i, j+1)))
            if visited!=fruits:
                return -1
            return out

        q = collections.deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((0, i, j))

        return bfs(q)
