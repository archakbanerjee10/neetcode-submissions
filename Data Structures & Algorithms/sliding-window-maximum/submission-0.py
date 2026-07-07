class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        result=[]
        for right in range(left+k-1,len(nums)):
            maximum=float("-inf")
            for i in range(left,right+1):
                maximum=max(maximum,nums[i])
            result.append(maximum)
            left+=1
        return result
        