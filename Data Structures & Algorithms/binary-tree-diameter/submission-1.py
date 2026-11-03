# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.d = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.d
    
    def traverse(self, root):
        if not root:
            return 0
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.d = max(self.d, left + right)
        return 1 + max(left, right)