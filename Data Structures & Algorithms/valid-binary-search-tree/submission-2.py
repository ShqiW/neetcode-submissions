# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # min.val < root.val < max.val
        return self._isValid(root, float('-inf'), float('inf'))

    def _isValid(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val <= minVal:
            return False
        if root.val >= maxVal:
            return False
        return self._isValid(root.left, minVal, root.val) and self._isValid(root.right, root.val, maxVal)
        