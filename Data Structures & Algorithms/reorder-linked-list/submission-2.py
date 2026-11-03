# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stk = []
        p = head
        while p:
            stk.append(p)
            p = p.next
        p = head
        while p:
            node = stk.pop()
            nxt_node = p.next
            if node == nxt_node or node.next == nxt_node:
                node.next = None
                break
            
            p.next = node
            node.next = nxt_node
            p = nxt_node
        