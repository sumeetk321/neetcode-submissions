"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d = dict()
        visited = set()
        def bfs(node, done):
            q = collections.deque()
            q.append(node)
            while q:
                top = q.popleft()
                if not top or top in visited:
                    continue
                visited.add(top)
                if not done:
                    d[top] = Node(top.val, None)
                if top:
                    for n in top.neighbors:
                        if done:
                            d[top].neighbors.append(d[n])
                        q.append(n)

        bfs(node, False)
        print(d)
        visited = set()
        bfs(node, True)
        return d[node]
        