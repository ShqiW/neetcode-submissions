# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.traverse(root)
        return self.max_sum
        
    
    def traverse(self, root):
        if not root:
            return 0
        left = max(self.traverse(root.left), 0)
        right = max(self.traverse(root.right), 0)
        self.max_sum = max(self.max_sum, left + root.val + right)
        return root.val + max(left, right)