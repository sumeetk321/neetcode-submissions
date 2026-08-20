class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i, target):
            if i >= len(candidates):
                if target==0 and sorted(sub) not in res:
                    res.append(sorted(sub.copy()))
                return
            sub.append(candidates[i])
            dfs(i+1, target-candidates[i])
            sub.pop()
            dfs(i+1, target)
        dfs(0, target)
        return res