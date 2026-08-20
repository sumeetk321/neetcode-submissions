class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [[float('inf')] * len(word2) for i in range(len(word1))]

        for i in range(len(word1)):
            if word2[-1] in word1[i:]:
                dp[i][-1] = len(word1[i:])-1
            else:
                dp[i][-1] = len(word1[i:])

        for j in range(len(word2)):
            if word1[-1] in word2[j:]:
                dp[-1][j] = len(word2[j:])-1
            else:
                dp[-1][j] = len(word2[j:])

        for i in range(len(word1)-2, -1, -1):
            for j in range(len(word2)-2, -1, -1):
                dp[i][j] = min(1+dp[i+1][j], 1+dp[i][j+1], (0 if word1[i]==word2[j] else 1)+dp[i+1][j+1])

        # for i in range(len(word1)):
        #     for j in range(len(word2)):
        #         print(dp[i][j], word1[i:], word2[j:])
        return dp[0][0]