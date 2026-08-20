class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2==1:
            return False
        target = target // 2
        dp = [False] * (target+1)
        dp[0] = True
        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] = dp[i] or dp[i-n]
        return dp[target]

            
