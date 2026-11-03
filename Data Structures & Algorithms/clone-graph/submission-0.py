"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = set()
        self.originToClone = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.traverse(node)
        return self.originToClone.get(node)
    
    def traverse(self, node):
        if not node:
            return
        if node in self.visited:
            return
        self.visited.add(node)
        if node not in self.originToClone:
            self.originToClone[node] = Node(node.val)
        cloneNode = self.originToClone[node]

        for neighbor in node.neighbors:
            self.traverse(neighbor)
            cloneNeighbor = self.originToClone[neighbor]
            cloneNode.neighbors.append(cloneNeighbor)
            
