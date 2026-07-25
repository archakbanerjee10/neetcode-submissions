class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lower_limit=0
        n=len(nums)
        needed_sum=(n*(n+1))//2
        array_sum=0
        for num in nums:
            array_sum+=num
        return needed_sum-array_sum

