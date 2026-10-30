class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum=0
        res=0
        mydict={0:1}

        for num in nums:
            currsum+=num
            diff=currsum-k
            res+=mydict.get(diff,0)
            mydict[currsum] = mydict.get(currsum, 0) + 1
        
        return res


        