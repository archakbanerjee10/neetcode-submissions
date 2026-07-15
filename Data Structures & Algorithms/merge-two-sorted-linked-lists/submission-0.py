# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the anchor for our new list
        dummy = ListNode(-1)
        # 2. head3 will be our active pointer to stitch the nodes together
        head3 = dummy
        
        # 3. Compare nodes until one list runs out
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                head3.next = list1  # Point head3's next to the smaller node
                list1 = list1.next  # Move list1 pointer forward
            else:
                head3.next = list2  # Point head3's next to the smaller node
                list2 = list2.next  # Move list2 pointer forward
            
            head3 = head3.next      # Move our stitching pointer forward
            
        # 4. If one list still has elements left, attach the entire remaining chain
        if list1 is not None:
            head3.next = list1
        else:
            head3.next = list2
            
        # 5. Return dummy.next (skips the -1 placeholder node)
        return dummy.next