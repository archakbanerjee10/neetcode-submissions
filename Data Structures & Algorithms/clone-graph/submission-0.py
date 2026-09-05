"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        

        oldtonew={}

        def dfs(node):
            #return the node if it is actually on the dictionary that means we have created the node copy prevuiously
            if node in oldtonew:
                return oldtonew[node]
            #making a copy of the present node 
            copy=Node(node.val)
            oldtonew[node]=copy
            #going through each and every neighbour of a node 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)