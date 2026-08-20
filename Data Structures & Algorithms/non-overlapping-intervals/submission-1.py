class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        pE = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= pE:
                pE = e
            else:
                res+=1
                pE = min(e, pE)
        return res