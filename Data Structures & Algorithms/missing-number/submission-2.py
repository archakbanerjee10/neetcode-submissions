class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        upper_limit=len(nums)
        if nums[0]!=0:
            return 0
        lower_limit=0
        higher_limit=nums[-1]
        for i in range(1,len(nums)):
            req_num=lower_limit+1
            if req_num != nums[i]:
                return req_num
            lower_limit+=1
        return upper_limit