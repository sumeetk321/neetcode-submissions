class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for i in range(len(text1))]

        for i in range(len(text1)):
            dp[i][-1] = 1 if text2[-1] in text1[i:] else 0
        for j in range(len(text2)):
            dp[-1][j] = 1 if text1[-1] in text2[j:] else 0

        for i in range(len(text1)-2, -1, -1):
            for j in range(len(text2)-2, -1, -1):
                if text1[i]==text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                #print(text1[i:], text2[j:], dp[i][j])
        # for row in dp:
        #     print(row)
        return dp[0][0]
