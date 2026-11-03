# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, float('-inf'))
        return self.res

    
    def traverse(self, node, maxVal):
        if not node:
            return 
        if node.val >= maxVal:
            maxVal = node.val
            self.res += 1
        self.traverse(node.left, maxVal)
        self.traverse(node.right, maxVal)

        