# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        slow=head
        fast=head
        dummy1=head
        while fast  and fast.next :
            fast=fast.next.next
            slow=slow.next
        dummy2=slow.next
        #breaking the link in between the arrays
        slow.next=None
        #reversing the second half of the linked  list
        curr=dummy2
        prev=None
        while curr is not None:
            Nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=Nextnode
        dummy2=prev
        while dummy2:
            nextnode1 = dummy1.next
            nextnode2 = dummy2.next
            
            dummy1.next = dummy2
            dummy2.next = nextnode1
            
            dummy1 = nextnode1
            dummy2 = nextnode2

        

        
            

        