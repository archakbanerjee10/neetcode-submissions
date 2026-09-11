class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)


        rob=[nums[0],max(nums[0],nums[1])]

        for i in range(2,n):
            robcost=max(nums[i]+rob[i-2],rob[i-1])
            rob.append(robcost)
        return rob[-1]
        
        
        