class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n
        leftProd=1
        for i in range(n):
            result[i]=leftProd
            leftProd*=nums[i]

        rightProd=1
        for i in range(n-1,-1,-1):
            result[i]*=rightProd
            rightProd*=nums[i]
        return result
            
        