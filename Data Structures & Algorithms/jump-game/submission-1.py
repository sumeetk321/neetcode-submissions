class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i]+1):
                if j+i >= len(nums)-1:
                    dp[i] = True
                    break
                elif dp[j+i]:
                    dp[i] = True
                    break
        return dp[0]