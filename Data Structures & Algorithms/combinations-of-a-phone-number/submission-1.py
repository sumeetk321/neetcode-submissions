class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ["a", "b" ,"c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"]
        , '5': ["j", "k", "l"], '6': ["m", "n", "o"], '7': ["p", "q", "r", "s"], 
        '8': ["t", "u", "v"], '9': ["w", "x", "y", "z"]}

        res = []
        sub = ""
        def dfs(i):
            nonlocal sub
            if i >= len(digits):
                if sub!="":
                    res.append(sub)
                return
            for c in d[digits[i]]:
                sub+=c
                dfs(i+1)
                sub = sub[:-1]
        
        dfs(0)
        return res
            