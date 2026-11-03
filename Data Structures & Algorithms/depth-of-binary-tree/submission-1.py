# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return 
        
        self.depth += 1
        self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        self.depth -= 1
        