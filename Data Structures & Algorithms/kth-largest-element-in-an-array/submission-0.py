class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)

        for i in range(k-1):
            heapq.heappop(maxHeap)
        
        return -1 * heapq.heappop(maxHeap)