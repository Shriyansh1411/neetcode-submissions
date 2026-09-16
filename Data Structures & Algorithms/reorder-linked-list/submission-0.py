# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        st=[]
        curr=head
        while curr:
            st.append(curr)
            curr=curr.next
        curr=head
        k=len(st)//2
        while (k>0):
            temp=curr.next
            top=st.pop()
            curr.next=top
            top.next=temp
            curr=temp
            k-=1
        curr.next=None
        return None
        