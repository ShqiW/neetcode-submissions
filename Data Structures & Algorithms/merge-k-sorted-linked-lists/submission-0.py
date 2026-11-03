# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        return self.mergeList(lists, 0, len(lists)-1)

    def mergeList(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start + end)//2
        left = self.mergeList(lists, start, mid)
        right = self.mergeList(lists, mid+1, end)
        return self.merge2list(left, right)
    
    def merge2list(self, l1, l2):
        p1, p2 = l1, l2
        dummy = ListNode()
        p = dummy

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next= p2
                p2 = p2.next
            p = p.next
        
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next