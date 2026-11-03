class Solution:
    def firstMissingPositive(self, a: list[int]) -> int:
        #neutralising the negastive elements of the array 
        for i in range(len(a)):
            if a[i]<0:
                a[i]=0
        
        #marking all the occurences of the numbers that are prositive
        for i in range(len(a)):
            val=abs(a[i])
            if 1<= val<=len(a):
                if a[val-1]>0:
                    a[val-1]*=-1
                elif a[val-1]==0:
                    #assigning a special value in this particular case 
                    a[val-1]=-1*(len(a)+1)
        
        #findin gout actually which element is missing 
        for i in range(1,len(a)+1):
            if a[i-1]>=0:
                return i
        
        return len(a)+1
