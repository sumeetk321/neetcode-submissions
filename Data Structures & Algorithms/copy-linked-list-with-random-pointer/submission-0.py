"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = Node(0)
        h1 = head
        d = dict()
        tmp = res
        while h1:
            res.next = Node(h1.val)
            d[h1] = res.next
            res = res.next
            h1 = h1.next
        h2 = head
        while h2:
            if h2.random:
                d[h2].random = d[h2.random]
            else:
                d[h2].random = None
            h2 = h2.next

        return tmp.next
        