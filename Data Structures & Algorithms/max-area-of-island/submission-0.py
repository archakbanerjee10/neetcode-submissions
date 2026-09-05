class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        visit=set()

        self.Maxarea=0

        def bfs(r,c):
            area=1
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row,col=q.popleft()
                directions=[[0,1],[0,-1],[1,0],[-1,0]]

                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc]==1:
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        area+=1
            self.Maxarea=max(self.Maxarea,area)
                



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    bfs(r,c)

        return self.Maxarea

        