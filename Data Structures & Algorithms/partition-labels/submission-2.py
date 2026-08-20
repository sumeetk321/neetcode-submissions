class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i, c in enumerate(s):
            if c not in m:
                m[c] = [i, i]
            m[c][1] = i
        print(m)
        minH = list(m.values())
        heapq.heapify(minH)
        res = []
        while minH:
            print(minH)
            pop1 = heapq.heappop(minH)
            if not minH:
                res.append(pop1[1]-pop1[0]+1)
                break
            pop2 = heapq.heappop(minH)
            if pop2[0] > pop1[1]:
                res.append(pop1[1]-pop1[0]+1)
                heapq.heappush(minH, pop2)
                continue
            else:
                heapq.heappush(minH, [min(pop1[0], pop2[0]), max(pop1[1], pop2[1])])
        return res

