# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #left_min < root.val < right_max
        def valid(node, left_min, right_max):
            if not node:
                return True
            if not (left_min < node.val < right_max):
                return False
            
            return valid(node.left, left_min, node.val) and valid(node.right, node.val, right_max)

        
        return valid(root, float("-inf"), float("inf"))