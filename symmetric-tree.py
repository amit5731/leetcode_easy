# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def check_and_provide(node, total=[]):
            if node.left == None and node.right == None:
                total.append("null_left")
                total.append(node.val)
                total.append("null_right")

            elif node.left == None and node.right:
                total.append("null_left")
                total.append(node.val)
                check_and_provide(node.right, total=total)
            elif node.right == None and node.left:
                check_and_provide(node.left, total=total)
                total.append(node.val)
                total.append("null_right")
            elif node.left and node.right:
                check_and_provide(node.left, total=total)
                total.append(node.val)
                check_and_provide(node.right, total=total)
            return total
        def change_node(node):
            if node.left==None and node.right:
                node.left,node.right=node.right,node.left
                change_node(node.left)
            elif node.left and node.right==None:
                node.left,node.right=node.right,node.left
                change_node(node.right)
            elif node.left==None and node.right==None:
                return
            elif node.left and node.right:
                node.left,node.right=node.right,node.left
                change_node(node.left)
                change_node(node.right)
        if not root:
            return root
        if root.right == None and root.left == None:
            return True
        if root.right == None or root.left == None:
            return False
        if root.right.val!=root.left.val:
            return False
        l1 = check_and_provide(root.left, total=[])
        change_node(root.right)
        l2 = check_and_provide(root.right, total=[])
        return l2==l1