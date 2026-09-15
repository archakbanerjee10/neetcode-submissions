class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total =sum(nums)

        if total%2 ==1:
            return False 
        
        required=total//2

        dp=set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            nextdp=set()
            for t in dp:
                nextdp.add(t+nums[i])
                nextdp.add(t)
            dp=nextdp

        return True if required in dp else False      
