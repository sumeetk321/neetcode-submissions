class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for i in range(len(s)+1)]
        dp[-1][-1] = True
        for j in range(len(p)-1, -1, -1):
            if p[j]=='*':
                dp[-1][j] = dp[-1][j+1]
                dp[-1][j-1] = dp[-1][j]
                j-=1
        for i in range(len(s)-1, -1, -1):
            for j in range(len(p)-1, -1, -1):
                if j < len(p)-1 and p[j+1]=='*':
                    dp[i][j] = dp[i][j+1]
                elif p[j]=='.':
                    dp[i][j] = dp[i+1][j+1]
                elif p[j]=='*':
                    dp[i][j] = dp[i][j+1] or (dp[i+1][j] if j > 0 and (p[j-1]==s[i] or p[j-1]=='.') else False)
                elif s[i]==p[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = False
        for i in range(len(s)):
            for j in range(len(p)):
                print((dp[i][j], s[i:], p[j:]))
        for r in dp:
            print(r)
        return dp[0][0]
