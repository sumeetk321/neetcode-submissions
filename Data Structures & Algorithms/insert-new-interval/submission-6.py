class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        added = False
        for i, iv in enumerate(intervals):
            if newInterval[0] < iv[0]:
                added = True
                if res and newInterval[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], newInterval[1])
                else:
                    res.append(newInterval)
                
                if iv[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], iv[1])
                else:
                    res.append(iv)
            else:
                res.append(iv)
        if not added:
            if res and newInterval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], newInterval[1])
            else:
                res.append(newInterval)
        return res

        