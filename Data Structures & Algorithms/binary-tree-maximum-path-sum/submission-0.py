# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.oneSideMax(root)
        return self.res
    
    def oneSideMax(self, root):
        if not root:
            return 0
        left_max_sum = max(0, self.oneSideMax(root.left))
        right_max_sum = max(0, self.oneSideMax(root.right))
        path_max_sum = root.val + left_max_sum + right_max_sum
        self.res = max(self.res, path_max_sum)
        return root.val + max(left_max_sum, right_max_sum)