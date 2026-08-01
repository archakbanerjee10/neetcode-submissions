# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False 
        
        # FIXED: Call isSameTree here instead of isSubtree to avoid infinite loop
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # FIXED: Moved out of isSubtree to be a peer function under the Solution class
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # FIXED: Properly indented under the isSameTree function scope
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        

    
        
        
        
        
        
