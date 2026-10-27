class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        #defining the merge function 
        def merge(arr,l,m,r):
            left=arr[l:m+1]
            right=arr[m+1:r+1]

            i,j,k=l,0,0

            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                arr[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                arr[i]=right[k]
                k+=1
                i+=1
            
            return arr        
        
        #defining the mergesort algorithm 
        def mergesort(arr,l,r):
            #base case

            if l>=r:
                return nums
            m=(l+r)//2

            #call mergesort recurssively
            #for the left half of the array 
            mergesort(arr,l,m)
            #for the right half of the array 
            mergesort(arr,m+1,r)

            #calling the merge function 
            merge(arr,l,m,r)

            return arr

        #call the mergesort function on the given array 
        return  mergesort(nums,0,len(nums)-1)


        