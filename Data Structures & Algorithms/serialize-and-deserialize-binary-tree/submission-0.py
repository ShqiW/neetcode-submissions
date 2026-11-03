# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def __init__(self):
        self.SEP = ','
        self.NULL = '#'
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = []
        self._serialize(root, string)
        return "".join(string)
    
    def _serialize(self, root, string):
        if not root:
            string.append(self.NULL + self.SEP)
            return
        string.append(str(root.val) + self.SEP)
        self._serialize(root.left, string)
        
        self._serialize(root.right, string)
        return root

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node = data.split(self.SEP)
        if node[-1] == '':
            node.pop()
        return self._deserialize(node)
    
    def _deserialize(self, node):
        if not node:
            return None
        first = node.pop(0)
        if first == self.NULL:
            return None
        root = TreeNode(int(first))
        root.left = self._deserialize(node)
        root.right = self._deserialize(node)
        return root
