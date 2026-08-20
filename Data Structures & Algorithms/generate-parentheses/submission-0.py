class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = ""
        def dfs(o, c):
            nonlocal sub
            if (o+c)>=2*n:
                res.append(sub)
                return
            if o < n:
                sub += "("
                dfs(o+1, c)
                sub = sub[:-1]
            if c+1 <= o:
                sub+=")"
                dfs(o, c+1)
                sub = sub[:-1]
            
        dfs(0, 0)
        return res
            