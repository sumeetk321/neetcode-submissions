class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i, target):
            if i >= len(nums) or target <= 0:
                if target==0:
                    res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i, target-nums[i])
            sub.pop()
            if i < len(nums)-1:
                dfs(i+1, target)
        dfs(0, target)
        return res