class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i=0
        while i<n-1 and nums[i]<nums[i+1]:
            i+=1
        left=0
        right=i
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        left=i+1
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1

        return -1
        