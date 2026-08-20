class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def dfs(num):
            if len(num)==0:
                res.append(sub.copy())
                return
            
            for i in range(len(num)):
                copy = num[0:i]+num[i+1:]
                sub.append(num[i])
                dfs(copy)
                sub.pop()
        dfs(nums)
        return res
