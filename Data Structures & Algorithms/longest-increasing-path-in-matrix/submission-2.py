class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = [[1]*len(matrix[i]) for i in range(len(matrix))]

        def dfs(i, j):
            if cache[i][j] > 1:
                return cache[i][j]
            else:
                m = 1
                if i > 0 and matrix[i-1][j]<matrix[i][j]:
                    m = max(m, 1+dfs(i-1,j))
                if i < len(matrix)-1 and matrix[i+1][j] < matrix[i][j]:
                    m = max(m, 1+dfs(i+1,j))
                if j > 0 and matrix[i][j-1] < matrix[i][j]:
                    m = max(m, 1+dfs(i,j-1))
                if j < len(matrix[0])-1 and matrix[i][j+1] < matrix[i][j]:
                    m = max(m, 1+dfs(i,j+1))
                cache[i][j] = m
                return m
        
        res = 0
        for i in range(len(cache)):
            for j in range(len(cache[0])):
                res = max(res, dfs(i, j))
        for r in matrix:
            print(r)
        for r in cache:
            print(r)
        return res
                    
