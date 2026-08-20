class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        for i in range(len(s)):
            l, r = i, i
            currlen = 1
            while l >= 0 and r <= len(s)-1 and s[l]==s[r]:
                currlen+=2
                l-=1
                r+=1
            
            if currlen > reslen:
                res = s[l+1:r]
                reslen = currlen

            l, r = i, i+1
            currlen = 2
            while l >= 0 and r <= len(s)-1 and s[l]==s[r]:
                currlen+=2
                l-=1
                r+=1

            if currlen > reslen:
                res = s[l+1:r]
                reslen = currlen
        
        return res