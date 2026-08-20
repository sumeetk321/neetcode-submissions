class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}

        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

        visited = set()

        q = collections.deque()
        q.append(0)

        while q:
            curr = q.popleft()

            if curr in visited:
                return False

            visited.add(curr)
            q.extend(adjList[curr])
            for neighbor in adjList[curr]:
                adjList[neighbor].remove(curr)

            adjList[curr] = []

        return len(visited)==n