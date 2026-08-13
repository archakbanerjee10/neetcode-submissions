# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        #returns the max value without splitting
        def dfs(root):
            if not root:
                return 0
            leftmax=dfs(root.left)
            rightmax=dfs(root.right)
            #handling negative cases
            leftmax=max(0,leftmax)
            rightmax=max(0,rightmax)

            #return the maximum value by splitting
            res[0]=max(res[0],root.val+leftmax+rightmax)

            return root.val+max(leftmax,rightmax)
        #calling the function on root of the tree
        dfs(root)
        return res[0]



            

        