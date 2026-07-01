class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            prod=1
            j=0
            while j<len(nums):
                if(i==j):
                    j+=1
                else:
                    prod*=nums[j]
                    j+=1
            result.append(prod)
        return result
        