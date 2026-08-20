class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        m = 0
        while r!=len(prices) and l!=len(prices):
            if prices[l] <= prices[r]:
                m = max(m, prices[r]-prices[l])
                r+=1
            else:
                l=r
                r=l+1
        return m