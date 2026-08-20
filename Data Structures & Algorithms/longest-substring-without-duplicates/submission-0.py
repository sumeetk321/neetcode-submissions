class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 1
        while r<=len(s):
            if r-l==len(set(s[l:r])):
                r+=1
                res = max(res, r-l-1)
            else:
                l+=1
        return res
            
            