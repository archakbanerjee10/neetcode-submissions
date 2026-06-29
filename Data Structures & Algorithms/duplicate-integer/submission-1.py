class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        dict={}
        for i in range(n):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]]=0
        return False