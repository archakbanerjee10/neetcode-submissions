class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        j=n-1
        i=0
        while(i<j):
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if(s[i].lower()==s[j].lower()):
                i+=1
                j-=1
            else:
                return False
        return True
            
    
            
            
            

        