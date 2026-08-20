class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minH = [[grid[0][0], 0, 0]]

        while minH:
            t, i, j = heapq.heappop(minH)

            if i < 0 or i >= n or j < 0 or j >= n or (i, j) in visited:
                continue

            if i==n-1 and j==n-1:
                return t
            
            visited.add((i, j))
            if i > 0:
                heapq.heappush(minH, [max(t, grid[i-1][j]), i-1, j])
            if j > 0:
                heapq.heappush(minH, [max(t, grid[i][j-1]), i, j-1])
            if i < n-1:
                heapq.heappush(minH, [max(t, grid[i+1][j]), i+1, j])
            if j < n-1:
                heapq.heappush(minH, [max(t, grid[i][j+1]), i, j+1])
            
