class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n-1 and nums[i]<nums[i+1]:
            i+=1
        new_arr=[]
        new_arr=nums[i+1:]+nums[0:i+1]
        return new_arr[0]

             

        