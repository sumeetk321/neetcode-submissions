class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curr = [['.'] * n for i in range(n)]
        res = []
        bR = set()
        bC = set()
        bUD = set()
        bLD = set()
        visited = set()
        def dfs(qu):
            # print(qu)
            # for r in curr:
            #     print(r)
            # print(visited)
            if qu>=n:
                currOut = [''.join(row) for row in curr]
                res.append(currOut)
                return
            else:
                for i in set(range(qu, n)).difference(bR):
                    for j in set(range(n)).difference(bC):
                        if curr[i][j]=='Q' or (i+j) in bUD or (i-j) in bLD or (i, j) in visited:
                            continue
                        curr[i][j] = 'Q'
                        bR.add(i)
                        bC.add(j)
                        bUD.add(i+j)
                        bLD.add(i-j)
                        dfs(qu+1)
                        bR.remove(i)
                        bC.remove(j)
                        bUD.remove(i+j)
                        bLD.remove(i-j)
                        curr[i][j] = '.'
        
        dfs(0)
        return res
