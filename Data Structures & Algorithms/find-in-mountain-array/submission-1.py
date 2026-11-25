class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

         
        length=mountainArr.length()
        #finding the peak
        l,r=1,length-2
        while l<=r:
            m=(l+r)//2
            left=mountainArr.get(m-1)
            mid=mountainArr.get(m)
            right=mountainArr.get(m+1)

            #we are in the left side of the mountain 
            if  left<mid<right:
                l=m+1
            #we are in the right side of the mountain 
            elif left>mid>right:
                r=m-1
            #we found the peak we are at the peak 
            else:
                break
        peak=m

        #first applying the binary search on the left side of the mountain 
        l=0
        r=peak
        while l<=r:
            m=(l+r)//2
            mid=mountainArr.get(m)
            if mid == target:
                return m 
            elif mid<target:
                l=m+1
            else:
                r=m-1

        #now appying the binary search on the right side of the mountain 
        l=peak
        r=length-1
        while l<=r:
            m=(l+r)//2
            mid=mountainArr.get(m)
            if mid==target:
                return m 
            elif mid<target:
                r=m-1
            else:
                l=m+1
        
        return -1
