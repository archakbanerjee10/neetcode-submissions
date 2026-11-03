class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i:int,j:int,st:str):
            while i<j:
                if st[i]!=st[j]:
                    return False 
                i+=1
                j-=1
            return True

        left=0
        right=len(s)-1
        while left<right:
            #on mismatch try skipping elements and checking 
            if s[left]!=s[right]:
                return is_palindrome(left+1,right,s) or is_palindrome(left,right-1,s)
            left+=1
            right-=1
        return True