# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        itr1=headA
        itr2=headB
        visited={}
        while itr1:
          visited[id(itr1)]=itr1.val
          itr1=itr1.next
        while itr2:
            if id(itr2) in visited:
                return itr2
            itr2=itr2.next
        
         
                
            
            
        
        
            
        
        