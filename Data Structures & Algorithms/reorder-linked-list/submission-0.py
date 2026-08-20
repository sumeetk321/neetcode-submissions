# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None
        prev = None
        while l2:
            n = l2.next
            l2.next = prev
            prev = l2
            l2 = n
        
        tmp = head
        l2 = prev
        while tmp and l2:
            n1 = tmp.next
            n2 = l2.next
            tmp.next = l2
            l2.next = n1
            tmp = n1
            l2 = n2
        return head