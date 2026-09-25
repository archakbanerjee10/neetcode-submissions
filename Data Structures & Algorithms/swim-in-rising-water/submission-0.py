class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #djikstras algo 
        #require minHeap (height,row,col)#height and coordinates of the input node 
        #greedy algorithm required 
        #thats why using this algorihtm 
        #uses visit hashset 
        #for finding the row with the max height 
        N=len(grid)
        visit=set()
        minH=[[grid[0][0],0,0]]#time,row,col
        heapq.heapify(minH)
        directions=[[0,1],[0,-1],[1,0],[-1,0]]

        visit.add((0,0))

        while minH:
            t,r,c=heapq.heappop(minH)
            if r==N-1 and c==N-1:
                return t
            
            for dr,dc in directions:
                neiR,neiC =r+dr,c+dc

                if neiR<0 or neiC<0 or neiR==N or neiC==N or ((neiR,neiC) in visit):
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minH,[max(t,grid[neiR][neiC]),neiR,neiC])
