class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachPac = set()
        reachAtl = set()

        def bfs(q, s):
            visited = set()
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                if i-1 >= 0 and heights[i-1][j] >= heights[i][j] and ((i-1, j)) not in visited:
                    s.add((i-1, j))
                    q.append((i-1, j))
                if i+1 < len(heights) and heights[i+1][j] >= heights[i][j] and ((i+1, j)) not in visited:
                    s.add((i+1, j))
                    q.append((i+1, j))
                if j-1 >= 0 and heights[i][j-1] >= heights[i][j] and ((i, j-1)) not in visited:
                    s.add((i, j-1))
                    q.append((i, j-1))
                if j+1 < len(heights[0]) and heights[i][j+1] >= heights[i][j] and ((i, j+1)) not in visited:
                    s.add((i, j+1))
                    q.append((i, j+1))
        q = collections.deque()
        for i in range(len(heights[0])):
            q.append((0, i))
            reachPac.add((0, i))
        for i in range(1, len(heights)):
            q.append((i, 0))
            reachPac.add((i, 0))
        bfs(q, reachPac)
        q = collections.deque()
        for i in range(len(heights[0])):
            q.append((len(heights)-1, i))
            reachAtl.add((len(heights)-1, i))
        for i in range(len(heights)-1):
            q.append((i, len(heights[0])-1))
            reachAtl.add((i, len(heights[0])-1))
        bfs(q, reachAtl)
        return [[i, j] for (i, j) in set.intersection(reachPac, reachAtl)]
