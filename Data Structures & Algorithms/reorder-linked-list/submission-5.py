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
            last_node = stk.pop()
            nxt = p.next
            if last_node == nxt or last_node.next == nxt:
                last_node.next = None
                break
            p.next = last_node
            last_node.next = nxt
            p = nxt
        