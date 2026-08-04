# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #level order traversal only print the right side value
        res=[]
        q=deque([root])

        while q:
            rightside=None
            qlen=len(q)

            for i in range(qlen):
                node=q.popleft()
                if node:
                    rightside=node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)
        return res


        
        