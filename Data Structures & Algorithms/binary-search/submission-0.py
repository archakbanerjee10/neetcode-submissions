class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            result=(left+right)//2
            if nums[result]==target:
                return result
            elif nums[result]>target:
                right=result-1
            else:
                left=result+1
        return -1


        