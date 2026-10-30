class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        currsum=0
        prefsums={0:1}

        for num in nums:
            currsum+=num
            diff=currsum-k
            res += prefsums.get(diff, 0)
            prefsums[currsum] = prefsums.get(currsum, 0) + 1


        return res

        