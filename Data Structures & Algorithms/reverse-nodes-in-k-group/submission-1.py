# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        a, b = head, head
        for i in range(k):
            if not b:
                return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead
    


    def reverse(self, a, b):
        pre = None
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
        