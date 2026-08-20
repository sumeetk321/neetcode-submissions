# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = None
        prev = None
        curr = head
        while curr:
            print(prev.val if prev else "None")
            i = 1
            currk = curr
            count = 0
            while currk and count < k:
                currk = currk.next
                count+=1
            if count < k:
                if prev:
                    prev.next = curr
                else:
                    res = curr
                break
            currk = curr
            prev1 = None
            tmp = None
            while currk and i <= k:
                i+=1
                print(currk.val, i)
                tmp = currk
                currk = tmp.next
                tmp.next = prev1
                prev1 = tmp
            
            if prev:
                prev.next = tmp
            else:
                res = tmp
            prev = curr
            curr = currk
        return res


            