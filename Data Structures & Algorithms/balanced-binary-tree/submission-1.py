# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        return 1 + max(left, right)
        