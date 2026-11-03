"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originClone = {}
        p = head
        while p:
            if p not in originClone:
                originClone[p] = Node(p.val)
            p = p.next
        p = head
        while p:
            if p.next:
                originClone[p].next = originClone[p.next]
            if p.random:
                originClone[p].random = originClone[p.random]
            p = p.next
        return originClone[head] if head else None     