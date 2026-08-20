# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = l1.val+l2.val
        digit = s%10
        carry = int(s/10)
        l1 = l1.next
        l2 = l2.next
        head = ListNode(digit, None)
        copy = head
        while l1 or l2:
            if l1 and l2:
                s = l1.val+l2.val
                digit = (s + carry)%10
                carry = int((s+carry)/10)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                digit = (l1.val+carry)%10
                carry = int((l1.val+carry)/10)
                l1 = l1.next
            elif l2:
                digit = (l2.val+carry)%10
                carry = int((l2.val+carry)/10)
                l2 = l2.next
            head.next = ListNode(digit, None)
            head = head.next
        if carry!=0:
            head.next = ListNode(carry, None)
        return copy