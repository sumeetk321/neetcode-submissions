class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pos(n):
            dp = [float('inf')] * (n+1)
            dp[0] = 1
            dp[1] = x
            def recursePos(n):
                if dp[n] != float('inf'):
                    return dp[n]
                
                if n%2==0:
                    tmp = recursePos(n // 2)
                    dp[n] = tmp*tmp
                else:
                    dp[n] = recursePos(n//2)*recursePos(n//2+1)

                return dp[n]
            return recursePos(n)
        def neg(n):
            dp = [float('inf')] * (n+1)
            dp[1] = 1.0/x
            def recurseNeg(n):
                if dp[n] != float('inf'):
                    return dp[n]
                
                if n%2==0:
                    tmp = recurseNeg(n // 2)
                    dp[n] = tmp*tmp
                else:
                    dp[n] = recurseNeg(n//2)*recurseNeg(n//2+1)

                return dp[n]
            return recurseNeg(n)
        if n==0:
            return 1
        if n > 0:
            return pos(n)
        else:
            return neg(-n)