class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr+=c.lower()
        
        p1 = 0
        p2 = len(newstr)-1
        while p2 >= p1:
            if newstr[p2]!=newstr[p1]:
                return False
            p1+=1
            p2-=1
        return True