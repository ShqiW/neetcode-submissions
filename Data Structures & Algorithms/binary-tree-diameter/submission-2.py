# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        throughNode = leftHeight + rightHeight

        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        return max(throughNode, left, right)
    
    def maxHeight(self, root):
        if not root:
            return 0
        return 1+ max(self.maxHeight(root.left), self.maxHeight(root.right))