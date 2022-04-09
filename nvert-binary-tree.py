# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def do_invert(node):
            if node.left==None and node.right==None:
                return
            node.left,node.right=node.right,node.left
            if node and node.left:
                do_invert(node.left)
            if node and node.right:
                do_invert(node.right)
        if not root:
            return root
        do_invert(root)
        return root