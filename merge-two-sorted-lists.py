# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        newnode=ListNode()
        itr1=list1
        itr2=list2
        temp=newnode
        while itr1 or itr2:
            if  itr1 and itr2 and (itr1.val<itr2.val):
                temp.next=ListNode(val=itr1.val)
                itr1=itr1.next
            elif itr1 and itr2 and (itr1.val>itr2.val):
                temp.next=ListNode(val=itr2.val)
                itr2=itr2.next
            elif itr1 and itr2 and (itr1.val==itr2.val):
                temp.next=ListNode(val=itr1.val)
                temp=temp.next
                temp.next=ListNode(val=itr2.val)
                itr2=itr2.next
                itr1=itr1.next
            elif not itr1:
                temp.next=ListNode(val=itr2.val)
                itr2=itr2.next
            elif not itr2:
                temp.next = ListNode(val=itr1.val)
                itr1 = itr1.next
            temp = temp.next
        newnode=newnode.next
        return newnode
