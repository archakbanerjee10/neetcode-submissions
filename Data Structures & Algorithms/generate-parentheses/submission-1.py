class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #we are creating a stack for holding up all the parenthesis
        stack=[]
        #res is initialized so i can return the result
        res=[]
        def dfs(opencount,closecount):
            #defining our base case 
            if opencount==closecount==n:
                #taking each charachter in the stack and joining them together in a string
                res.append("".join(stack))
                return 
            #condition where we are adding the open bracket 
            if opencount<n:
                stack.append("(")
                dfs(opencount+1,closecount)
                stack.pop()
            #condition where we are adding the closing bracket 
            if closecount<opencount:
                stack.append(")")
                dfs(opencount,closecount+1)
                stack.pop()
        dfs(0,0)
        return res 


                
            
            

        