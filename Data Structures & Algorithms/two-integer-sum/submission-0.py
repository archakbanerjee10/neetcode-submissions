class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        dict1={}
        for i in range(n):
            complement=target-nums[i]
            if complement not in dict1:
                dict1[nums[i]]=i
            else:
                return list([dict1[complement],i])
        