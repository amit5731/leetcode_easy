# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        total=[]
        def check_and_provide(node):
            if node.left==None and node.right:
                total.append(node.val)
                check_and_provide(node.right)
            elif node.right==None and node.left:
                check_and_provide(node.left)
                total.append(node.val)
            elif node.right==None and node.left==None:
                total.append(node.val)
            elif node.left and node.right:
                check_and_provide(node.left)
                total.append(node.val)
                check_and_provide(node.right)            
        if not root:
            return root
        check_and_provide(root)
        return total
        
            
            
            
        
            
        
            
        