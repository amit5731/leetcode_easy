# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       self.visited=0
       def dfs(node):
            if not node:
                return -1
            left=dfs(node.left)
            right=dfs(node.right)
            self.visited=max(self.visited,left+right+2)#BASICALLY THIS IS THE FORMULLA OF DIAMETER (LEFT HEIGHT+RIGHT HEIGHT +1) TO MINIMIZE -1 WE ADD +1
            return max(left,right)+1#NODES=EDGES+1 AS WE CAN CHECKING MAX NODES FROM A ROOT NODE WE ARE TAKING MAX.
       dfs(root)
       return self.visited
            
            