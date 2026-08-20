class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            s1 = -1 * heapq.heappop(maxHeap)
            s2 = -1 * heapq.heappop(maxHeap)
            if s1 < s2:
                s2 = s2 - s1
                heapq.heappush(maxHeap, -1 * s2)
            elif s1 > s2:
                s1 = s1 - s2
                heapq.heappush(maxHeap, -1 * s1)
        if len(maxHeap)==1:
            return -1 * maxHeap[0]
        return 0