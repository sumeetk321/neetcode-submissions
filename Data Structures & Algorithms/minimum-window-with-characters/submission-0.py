class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isPresent(c, te):
            for k in te.keys():
                if k not in c.keys() or c[k] < te[k]:
                    return False
            return True
                
        l = 0
        r = 0
        count = dict()
        tcount = dict()
        res = ""
        for c in t:
            tcount[c] = tcount.get(c, 0)+1
        while r < len(s):
            while r < len(s) and not isPresent(count, tcount):
                count[s[r]] = count.get(s[r], 0)+1
                r+=1
            while isPresent(count, tcount):
                res = s[l:r]
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
        return res
            