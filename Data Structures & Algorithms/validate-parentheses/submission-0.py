from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        brack_dict={')':'(',"]":'[','}':'{'}
        for brackets in s:
            if   brackets in brack_dict:
                if stack and stack[-1]==brack_dict[brackets]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brackets)
        if len(stack)==0:
            return True
        return False

            

        