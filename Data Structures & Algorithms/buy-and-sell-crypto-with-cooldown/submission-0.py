class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, bought):
            if i>=len(prices):
                return 0
            if (i, bought) in memo.keys():
                return memo[(i, bought)]
            if not bought:
                memo[(i, bought)] = max(-prices[i]+dp(i+1, True), dp(i+1, False))
            else:
                memo[(i, bought)] = max(prices[i]+dp(i+2, False), dp(i+1, True))
            return memo[(i, bought)]
        #dp(0, False)
        #print(memo)
        return dp(0, False)

        