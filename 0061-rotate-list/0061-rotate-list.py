class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return None
        
        # 1. Fixed length count (start at 1)
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
            
        k = k % length
        if k == 0:
            return head
            
        # Making it a circular linked list
        cur.next = head
        newtail = length - k
        current = head
        
        for _ in range(newtail - 1):
            current = current.next
            
        nexthead = current.next
        current.next = None
        
        # 2. Return nexthead instead of current
        return nexthead