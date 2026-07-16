# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node=head
        length=0
        while  node :
            length+=1
            node=node.next
        steps_to_move = length - n
        curr = dummy
        for _ in range(steps_to_move):
            curr = curr.next
        curr.next=curr.next.next

        return dummy.next
        

        