# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val <= list2.val:
            head=list1
            temp1=list1.next
        else:
            head=list2
            temp2=list2.next
        prev=head
        while temp1 and temp2:
            if temp1.val <= temp2.val :
                prev.next=temp1
                prev=temp1
                temp1=temp1.next 
            else:
                prev.next=temp2
                prev=temp2
                temp2=temp2.next
        prev.next=temp1 or temp2
        return head
        