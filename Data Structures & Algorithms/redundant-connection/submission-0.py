class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        #maintaining the parent of every single node 
        par=[i for i in range(len(edges)+1)]
        #rank of  each component
        rank=[1]*(len(edges)+1)

        #defining the function of find to find the root node of each component 
        def find(n):
            while n!=par[n]:
                par[n]=par[par[n]]#path compression 
                n=par[n]
            return n
            

        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False 
            
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]

            return True 

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
