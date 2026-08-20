class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        p = -1
        res = 0
        revL = []
        x = abs(x)
        while x:
            #print(x)
            revL.append(x%10)
            p+=1
            x = x // 10
        
        for d in revL:
            res+=d*(10**p)
            p-=1
        
        if neg:
            res = -res

        if res < -(2**31) or res > (2**31)-1:
            return 0
        
        return res