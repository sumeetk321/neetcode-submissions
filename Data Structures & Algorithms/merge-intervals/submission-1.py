class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda r: (r[0], r[1]))
        print(intervals)
        res = []
        i = 0
        while i < len(intervals):
            l = intervals[i][0]
            r = intervals[i][1]
            while i < len(intervals)-1 and intervals[i+1][0] <= r:
                r = max(r, intervals[i+1][1])
                i+=1
            res.append([l, r])
            i+=1
            
        return res
