# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head=ListNode()
        dummy=head
        if len(lists) ==0:
            return dummy.next
        i=0
        length=len(lists)
        new_arr=[]
        while i<length:
            while lists[i]:
                new_arr.append(lists[i].val)
                lists[i] = lists[i].next
            i+=1
        new_arr.sort()
        for num in new_arr:
            dummy.next=ListNode(num)
            dummy=dummy.next
        return head.next


        
        