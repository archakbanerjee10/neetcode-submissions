class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(st:str,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False 
                i+=1
                j-=1
            return True
        
        left=0
        right=len(s)-1

        while left<right:
            #check only when there actually is a mismatch
            if s[left]!=s[right]:
                return is_palindrome(s,left+1,right) or is_palindrome(s,left,right-1)
            left+=1
            right-=1

        return True 