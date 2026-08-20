# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = ListNode()
        res = tmp
        newlist = lists.copy()
        while any(x for x in newlist):
            node = None
            idx = 0
            minval = float('inf')

            for i in range(len(lists)):
                n = newlist[i]
                if not n:
                    continue
                if n.val < minval:
                    minval = n.val
                    idx = i
                    node = n
            newlist[idx] = node.next
            node.next = None
            tmp.next = node
            tmp = tmp.next

        return res.next
