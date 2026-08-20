class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = Counter(hand)
        minH = list(m.keys())
        heapq.heapify(minH)

        while minH:
            popped = []
            for i in range(groupSize):
                if not minH:
                    return False
                pop = heapq.heappop(minH)
                if popped and (pop!=popped[-1]+1 or m[pop]==0):
                    return False
                popped.append(pop)
                m[pop]-=1
            for p in popped:
                if m[p] > 0:
                    heapq.heappush(minH, p)
        
        return True
            

