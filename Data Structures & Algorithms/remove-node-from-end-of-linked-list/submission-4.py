# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # 虚拟头节点
        fast = dummy
        
        for _ in range(n + 1):    # fast 先走 n+1 步
            fast = fast.next
        
        slow = dummy
        while fast:               # fast 到末尾时，slow 恰好在待删节点前一位
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next         # 返回 dummy.next 而非 head，防止头节点被删的情况