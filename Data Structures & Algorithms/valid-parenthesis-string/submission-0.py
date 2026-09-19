class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        stack2=[]
        count=0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == "*":
                stack2.append(i)
            elif c == ")":
                # Prefer matching with an actual '(' first
                if stack:
                    stack.pop()
                # Otherwise, use a '*' as a '('
                elif stack2:
                    stack2.pop()
                else:
                    return False
        
        while stack and stack2 :
            if stack[-1]<stack2[-1]:
                stack.pop()
                stack2.pop()
            else:
                return False 
        return len(stack)==0       