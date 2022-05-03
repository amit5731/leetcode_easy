# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        first=head
        second=head
        for i in range(n):
            second=second.next
        while first :
                if not second:
                    first=first.next
                    return first
                elif  second.next==None:
                    first.next=first.next.next
                    break
                first=first.next
                second=second.next
        return head
            