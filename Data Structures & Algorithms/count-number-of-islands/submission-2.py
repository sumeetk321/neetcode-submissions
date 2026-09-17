class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()

        visited = set()

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='0' or ((i, j) in visited):
                    continue
                queue = deque([(i, j)])
                while queue:
                    curri, currj = queue.popleft()
                    if (curri, currj) in visited or curri < 0 or curri >= len(grid) or currj < 0 or currj >= len(grid[0]) or grid[curri][currj]=='0':
                        continue
                    visited.add((curri, currj))

                    queue.extend([(curri+1, currj), (curri-1, currj), (curri, currj+1), (curri, currj-1)])
                
                res += 1
        
        return res
                        

        