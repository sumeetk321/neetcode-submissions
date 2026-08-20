class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def dfs(i, palin):
            print(i, palin)
            if i >= len(s):
                if palin==palin[::-1]:
                    if palin!="":
                        sub.append(palin)
                        res.append(sub.copy())
                        sub.pop()
                    else:
                        res.append(sub.copy())
                return
            
            if palin==palin[::-1] and palin!="":
                sub.append(palin)
                dfs(i+1, s[i])
                sub.pop()

            dfs(i+1, palin+s[i])

        dfs(0, "")
        return res