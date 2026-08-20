class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for i in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
        for i in range(1, amount+1):
            if i%coins[0]==0:
                dp[0][i] = 1
        for j in range(1, amount+1):
            for i in range(1, len(coins)):
                dp[i][j] = dp[i-1][j]+(dp[i][j-coins[i]] if j-coins[i] >= 0 else 0)
        # for r in dp:
        #     print(r)
        return dp[-1][-1]