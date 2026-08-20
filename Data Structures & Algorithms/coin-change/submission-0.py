class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')] * (amount+1)
        arr[0] = 0
        for i in range(1, amount+1):
            
            for c in coins:
                if i-c < 0:
                    continue
                arr[i] = min(arr[i], 1+arr[i-c])
            
        return (-1 if arr[-1]==float('inf') else arr[-1])