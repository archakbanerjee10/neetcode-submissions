class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #no extra space to be taken mentioned in the question 
        

        #handling the edge case 
        if not grid:
            return None

        
        dist=0
        ROWS,COLS=len(grid),len(grid[0])
        q=collections.deque()
        visit=set()

        #defining the addroom function 
        def addroom(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==-1  or (r,c) in visit:
                return 
            q.append([r,c])
            visit.add((r,c))


        #we are collectiung the indexes of all  the treausres that are in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid [r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))

        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist 
                #adding the cells in all the four directions 
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)

            #everytime the loop gets end we must add 1 to the disteance
            dist+=1

