class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[-1]
        if n==2:
            return max(nums)


        def helper(nums):
            s=len(nums)
            rob=[nums[0],max(nums[0],nums[1])]

            for i in range(2,s):
               robcost=max(nums[i]+rob[i-2],rob[i-1])
               rob.append(robcost)
            return rob[-1]
        
        including_first=helper(nums[1:])
        including_last=helper(nums[:n-1])
        return max(including_first,including_last)



        