class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            submap = {}
            for i in range(len(s)):
                if s[i] in submap:
                    submap[s[i]]+=1
                else:
                    submap[s[i]] = 1
            submap = tuple(sorted(submap.items()))
            if submap not in hm:
                hm[submap] = [s]
            else:
                hm[submap].append(s)
        out = []
        for k in hm.keys():
            out.append(hm[k])
        return out