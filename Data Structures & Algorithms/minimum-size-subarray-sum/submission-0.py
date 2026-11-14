class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sorting the array 
        low,high=0,0
        res=float("inf")
        total=0
        for high in range(len(nums)):
            #hiring
            total+=nums[high]
            #firing
            while total>=target:
                res=min(res,high-low+1)
                total-=nums[low]
                low+=1
                
        return res if res!=float("inf") else 0



            




        