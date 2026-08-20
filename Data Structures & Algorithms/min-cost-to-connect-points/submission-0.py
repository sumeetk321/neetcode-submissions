class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])

        visited = set()
        minH = [[0, 0]]
        res = 0
        while len(visited) < n:
            minEdge, node = heapq.heappop(minH)
            if node in visited:
                continue
            res+=minEdge
            visited.add(node)
            for newEdge, newNode in adjList[node]:
                heapq.heappush(minH, [newEdge, newNode])
        return res

