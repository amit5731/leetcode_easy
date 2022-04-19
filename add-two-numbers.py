# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        itr1=l1
        itr2=l2
        res1=""
        res2=""
        while itr1 or itr2:
            if itr1:
                res1+=str(itr1.val)
                itr1=itr1.next
            if itr2:
                res2+=str(itr2.val)
                itr2=itr2.next
        res2=str(int(res1[::-1])+int(res2[::-1]))[::-1]
        newnode=ListNode(val=res2[0])
        itr3=newnode
        for data in res2[1:] :
            #print(data)
            itr3.next=ListNode(val=data)
            itr3=itr3.next
            
        return newnode