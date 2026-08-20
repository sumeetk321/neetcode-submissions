class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        off = 1
        for i in range(1, n+1):
            if off*2==i:
                off = i
            dp[i] = 1+dp[i-off]
        return dp