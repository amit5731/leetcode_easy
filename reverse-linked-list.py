# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        if not head:
            return head
        res=ListNode(val=itr.val,next=None)
        itr=itr.next
        while itr:
            res=ListNode(val=itr.val,next=res)
            itr=itr.next
        return res
            
            
        