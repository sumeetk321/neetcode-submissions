class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            ones = 0
            tmp = i
            while tmp:
                ones+=tmp%2
                tmp = tmp >> 1
            res.append(ones)
        return res