class MedianFinder:

    def __init__(self):
        self.lH = []
        self.uH = []

    def addNum(self, num: int) -> None:
        if len(self.lH)==0:
            heapq.heappush(self.lH, -num)
        else:
            if num > -self.lH[0]:
                heapq.heappush(self.uH, num)
                if len(self.uH)-len(self.lH) > 1:
                    pop = heapq.heappop(self.uH)
                    heapq.heappush(self.lH, -pop)
            else:
                heapq.heappush(self.lH, -num)
                if len(self.lH)-len(self.uH) > 1:
                    pop = heapq.heappop(self.lH)
                    heapq.heappush(self.uH, -pop)

    def findMedian(self) -> float:
        if len(self.lH)-len(self.uH)==0:
            return (-self.lH[0]+self.uH[0])/2
        elif len(self.lH)-len(self.uH)==1:
            return -self.lH[0]
        else:
            return self.uH[0]
        