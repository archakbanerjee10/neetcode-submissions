class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        nums.sort()
        res=[]
        length=len(nums)/3
        left=0
        right=0
        while left<len(nums):
            while right<len(nums) and nums[left]==nums[right]:
                right+=1
            total=right-left
            if total>length:
                res.append(nums[left])
            left=right
        return res
        