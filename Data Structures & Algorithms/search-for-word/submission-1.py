class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS=len(board),len(board[0])
        path=set()

        def dfs(r,c,i):
            #base case handling 
            if i==len(word):
                return True
            
            
            #returning false base cases 
            if (r>=ROWS or c>=COLS or i>len(word) or r<0 or c<0 or board[r][c]!=word[i] or (r,c) in path):
                return False 
            
            
            #adding r, c to the visited set 
            path.add((r,c))
            #calling the dfs function for four cases for each element in board 

            res=dfs(r+1,c,i+1)or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            #removing r,c from the visited set 
            path.remove((r,c))
            return res 
        #calling the dfs function 
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0) : return True 

        #returning false if netiher of the elements in the board were able to sati sfy the condition 
        return False 

            

