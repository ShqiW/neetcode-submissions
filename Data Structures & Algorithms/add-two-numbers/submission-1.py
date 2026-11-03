# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            cur_node = ListNode(total % 10)
            p.next = cur_node
            p = p.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy.next
            
        

        