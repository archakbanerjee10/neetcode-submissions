class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        def reverse(nums:list,left:int,right:int):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left,right=left+1,right-1
            return nums 
        
        #need to csll this helper function for three times 

        #reversing the whole of the array 
        nums=reverse(nums,0,len(nums)-1)

        #reversing upto k 
        nums=reverse(nums,0,k-1)

        #reversing the rest of the array 
        nums=reverse(nums,k,len(nums)-1)