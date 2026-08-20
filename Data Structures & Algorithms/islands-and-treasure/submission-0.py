class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        # for r in grid:
        #     print (r)
        def bfs(q):
            
            while q:
                
                i, j = q.popleft()
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited:
                    continue
                visited.add((i,j))
                if grid[i][j]!=-1:
                    if (i, j)==(1, 0) or (i, j)==(0 ,0):
                        print ("in here")
                        for r in grid:
                            print (r)
                        print()
                    if i+1 < len(grid) and grid[i+1][j]!=-1:
                        grid[i][j] = min(grid[i][j], 1+grid[i+1][j])
                    if i-1 >= 0 and grid[i-1][j]!=-1:
                        grid[i][j] = min(grid[i][j], 1+grid[i-1][j])
                    if j+1 < len(grid[0]) and grid[i][j+1]!=-1:
                        grid[i][j] = min(grid[i][j], 1+grid[i][j+1])
                    if j-1 >= 0 and grid[i][j-1]!=-1:
                        grid[i][j] = min(grid[i][j], 1+grid[i][j-1])
                    q.append((i, j-1))
                    q.append((i, j+1))
                    q.append((i+1, j))
                    q.append((i-1, j))
                print((i, j))
                # for r in grid:
                #     print (r)
                # print()
            return
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i, j))
        bfs(q)
        return