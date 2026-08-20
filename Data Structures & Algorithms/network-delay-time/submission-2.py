class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = {i:[] for i in range(1, n+1)}

        for ui, vi, ti in times:
            adjList[ui].append([ti, vi])
        
        minH = [[0, k]]
        visited = set()
        while minH:
            time, node = heapq.heappop(minH)
            print(time, node)
            if node in visited:
                continue
            visited.add(node)
            if len(visited)==n:
                return time
            
            for ti, vi in adjList[node]:
                heapq.heappush(minH, [time+ti, vi])

        return -1
            