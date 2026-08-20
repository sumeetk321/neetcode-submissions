# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        n = ListNode()
        d = n
        while list1 and list2:
            if list1.val < list2.val:
                n.next = list1
                list1 = list1.next
            else:
                n.next = list2
                list2 = list2.next
            n = n.next
        if list1:
            n.next = list1
        elif list2:
            n.next = list2
        return d.next