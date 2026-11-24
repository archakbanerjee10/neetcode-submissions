class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def helper(largestSum):
            total = 0
            count = 1
            for n in nums:
                total+=n
                if total>largestSum:
                    total=n
                    count+=1
                    if count>k:
                        return False
            return True
        left,right = max(nums),sum(nums)
        while left<right:
            mid = left  + ( right-left)//2
            if helper(mid):
                right=mid
            else:
                left = mid+1
        return left   