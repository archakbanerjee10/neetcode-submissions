"""
# Definition for a copy.
class copy:
    def __init__(self, x: int, next: 'copy' = None, random: 'copy' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[copy]') -> 'Optional[copy]':
        hash_map={None:None}

        curr=head
        while curr:
            copy=Node(curr.val)
            hash_map[curr]=copy
            curr=curr.next
        
        dummy=head
        while dummy:
            copy=hash_map[dummy]
            copy.next=hash_map[dummy.next]
            copy.random=hash_map[dummy.random]
            dummy=dummy.next
        return hash_map[head]
        
        