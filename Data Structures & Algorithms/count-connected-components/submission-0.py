class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}

        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

        visited = set()
        def dfs(i):
            q = collections.deque()
            q.append(i)

            while q:
                curr = q.popleft()

                if curr in visited:
                    continue

                visited.add(curr)
                q.extend(adjList[curr])
                for neighbor in adjList[curr]:
                    adjList[neighbor].remove(curr)

                adjList[curr] = []

        res = 0
        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i)
        return res
