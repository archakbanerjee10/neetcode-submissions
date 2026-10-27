class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            #partition
            if nums[i]!=val:
                #we would keep this in nums
                nums[k]=nums[i]
                k+=1
        return k
            

        