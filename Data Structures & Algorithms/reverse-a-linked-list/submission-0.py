# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        newhead = None
        while head:
            tmp = head.next
            if tmp==None:
                newhead = head
            head.next = prev
            prev = head
            head = tmp
        return newhead