class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(cap):
            day=1
            currCap=cap
            for w in weights:
                if currCap-w<0:
                    currCap=cap
                    day+=1
                currCap-=w
            
            return day <= days
                

        #as the packages must be shipped within days we cant sort the array 
        maximum=sum(weights)
        minimum=max(weights)
        res=maximum
        while minimum<=maximum:
            mid=(maximum+minimum)//2
            if helper(mid):
                res=min(mid,res)
                #shrinking the window 
                maximum=mid-1
            else:
                #increasing the window 
                minimum=mid+1
        return res 
            




        

        