class Solution:
    def canJump(self, nums: List[int]) -> bool: 

        index=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=index:
                index=i

        return True if index==0 else False



        
        