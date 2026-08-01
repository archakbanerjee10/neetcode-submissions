# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        #handling the edge case if the tree is empty 
        if not root:
            return result
        #defining a double ended queue 
        q=collections.deque()
        #appending the root into the dequeue
        q.append(root)
        #looping through the tree
        while q:
            qlen=len(q)
            #initializing an empty array for each level 
            level=[]
            for i in range(qlen):
                node=q.popleft()
                #checking if the node is empty or not
                if node:
                    #appending the values into the level array
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                result.append(level)
        return result

        