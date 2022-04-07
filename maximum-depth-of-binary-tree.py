# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def check_depth(node, count=1):
            if not node:
                return count
            elif node.left and node.right:
                count+=1
                return max(check_depth(node.left, count=count),check_depth(node.right, count=count))
            elif node.left:
                count += 1
                return check_depth(node.left, count=count)
            elif node.right:
                count += 1
                return check_depth(node.right, count=count)
            elif node.left == None and node.right == None:
                return count
            return count

        if not root:
            return 0
        ch = 0
        ch2 = 0
        if root.left:
            ch = check_depth(root.left, count=1)
        if root.right:
            ch2 = check_depth(root.right, count=1)
        return max(ch, ch2) +1