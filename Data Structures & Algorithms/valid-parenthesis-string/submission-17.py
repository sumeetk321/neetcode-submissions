class Solution:
    def checkValidString(self, s: str) -> bool:
        maxL, minL = 0, 0
        for c in s:
            if c=='(':
                minL+=1
                maxL+=1
            elif c==')':
                minL-=1
                maxL-=1
            elif c=='*':
                minL-=1
                maxL+=1
            if minL < 0:
                minL = 0
            if maxL < 0:
                return False
        return minL<=0