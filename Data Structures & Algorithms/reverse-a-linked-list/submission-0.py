# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle the empty list case
        if head is None:
            return None
        
        prev = None
        current = head
        
        while current is not None:
            nextNode = current.next  # Save the next node
            current.next = prev      # Reverse the pointer
            prev = current           # Move prev forward
            current = nextNode       # Move current forward
            
        # prev will be pointing to the new head of the reversed list
        return prev

        