class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        arr = [0 for i in range(n)]
        arr[n-1] = 1
        arr[n-2] = 2
        for i in range(n-3, -1, -1):
            arr[i] = arr[i+1]+arr[i+2]
        return arr[0]
