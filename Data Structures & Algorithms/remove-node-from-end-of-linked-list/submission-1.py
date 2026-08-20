# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        i=0
        while copy:
            copy = copy.next
            i+=1
        print(i)
        j = 0
        copy = head
        if i==n:
            return head.next
        while head:
            if j==i-n-1:
                print("in here")
                head.next = head.next.next
                return copy
            head = head.next
            j+=1
        return copy
            