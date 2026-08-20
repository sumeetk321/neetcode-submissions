class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = [[0] * len(t) for i in range(len(s))]

        for i in range(len(s)):
            dp[i][-1] = (s[i:]).count(t[-1])
        for j in range(len(t)):
            dp[-1][j] = 1 if s[-1]==t else max(0, dp[-1][j])

        for i in range(len(s)-2, -1, -1):
            for j in range(len(t)-2, -1, -1):
                if s[i]==t[j]:
                    dp[i][j] = dp[i+1][j+1]+dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        for r in dp:
            print(r)
        return dp[0][0]
        