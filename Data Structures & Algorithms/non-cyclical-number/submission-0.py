class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n!=1:
            if n in visited:
                return False
            visited.add(n)
            tmp = 0
            while n:
                tmp+=(n%10)**2
                n = n // 10
            n = tmp
        return True