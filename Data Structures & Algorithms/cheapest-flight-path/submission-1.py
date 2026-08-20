class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i:[] for i in range(n)}

        for fr, to, price in flights:
            adjList[fr].append([price, to])

        #price, stops, node
        minH = [[0, 0, src]]
        visited = set()
        while minH:
            #print(minH)
            price, stops, node = heapq.heappop(minH)
            if stops > k+1 or (stops, node) in visited:
                continue
            if node==dst:
                return price
            visited.add((stops, node))
            for neiPrice, nei in adjList[node]:
                heapq.heappush(minH, [neiPrice+price, stops+1, nei])
        
        return -1
