class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(l):
            c = []
            for x in l:
                if x.isnumeric():
                    if int(x) in c:
                        return False
                    elif 1 <= int(x) and int(x) <= 9:
                        c.append(int(x))
                    else:
                        return False
                elif x=='.':
                    continue
                else:
                    return False
            return True
        for i in range(9):
            if not isValid(board[i]) or not isValid([b[i] for b in board]):
                return False
            row = int(int(i/3)*3)
            col = int((i%3)*3)
            boxlist = []
            for j in range(row, row+3):
                for k in range(col, col+3):
                    boxlist.append(board[j][k])
            if not isValid(boxlist):
                return False
        return True
