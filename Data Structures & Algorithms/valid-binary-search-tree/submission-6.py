# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, low, high = q.popleft()

            # The current node MUST strictly stay inside (low, high)
            if not (low < node.val < high):
                return False

            # Going left updates the upper bound to node.val
            if node.left:
                q.append((node.left, low, node.val))
            
            # Going right updates the lower bound to node.val
            if node.right:
                q.append((node.right, node.val, high))

        return True
        
        