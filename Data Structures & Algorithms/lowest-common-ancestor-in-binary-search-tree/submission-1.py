class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 保证 val1 较小，val2 较大
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        return self.find(root, val1, val2)

    # 在 BST 中寻找 val1 和 val2 的最近公共祖先节点
    def find(self, root: 'TreeNode', val1: int, val2: int) -> 'TreeNode':
        if root is None:
            return None
        if root.val > val2:
            # 当前节点太大，去左子树找
            return self.find(root.left, val1, val2)
        if root.val < val1:
            # 当前节点太小，去右子树找
            return self.find(root.right, val1, val2)
        # val1 <= root.val <= val2
        # 则当前节点就是最近公共祖先
        return root
        