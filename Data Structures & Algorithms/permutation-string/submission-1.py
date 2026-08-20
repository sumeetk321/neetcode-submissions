class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s = dict()
        for c in s1:
            s[c] = s.get(c, 0)+1
        ns = dict()
        for i in range(len(s1)):
            ns[s2[i]] = ns.get(s2[i], 0)+1
        if ns==s:
            return True
        l = 0
        r = len(s1)-1
        while r<len(s2):
            ns[s2[l]]-=1
            if ns[s2[l]]==0:
                ns.pop(s2[l], None)
            l+=1
            r+=1
            if r >= len(s2):
                break
            ns[s2[r]] = ns.get(s2[r], 0)+1
            if ns==s:
                return True
        return False