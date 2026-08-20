class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c)-97] += 1
            m[tuple(letters)].append(s)

        res = []
        for val in m.values():
            res.append(val)
        return res