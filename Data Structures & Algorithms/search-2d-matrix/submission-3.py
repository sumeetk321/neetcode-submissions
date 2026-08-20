class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1
        while l<r:
            mid = l+(r-l)//2
            row = int(mid/n)
            col = mid%n
            if matrix[row][col] >= target:
                r = mid
            else:
                l = mid+1
        row = int(l/n)
        col = l%n
        print(l, row, col)
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        return matrix[row][col] == target