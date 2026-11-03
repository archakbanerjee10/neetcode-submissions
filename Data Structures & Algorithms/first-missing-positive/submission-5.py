class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        maximum=max(nums)
        for i in range(1,n+1):
            if i not in nums:
                return i
        if maximum<0:
            return 1
        else:
            return maximum+1
        