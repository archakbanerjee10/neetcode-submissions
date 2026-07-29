# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        #calculating the left subtree first
        leftside_length=self.maxDepth(root.left)
        #calculating the length of the right subtree
        rightside_length=self.maxDepth(root.right)
        #returning 1 more to the max because of the root 
        return 1+max(leftside_length,rightside_length)
        
        