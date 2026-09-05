class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        my_dict={}
        for i in range(n):
            if nums[i] in my_dict :
                my_dict[nums[i]]+=1
                if my_dict[nums[i]]>=n/2:
                    return nums[i]
            else:
                my_dict[nums[i]]=1
        return nums[-1]