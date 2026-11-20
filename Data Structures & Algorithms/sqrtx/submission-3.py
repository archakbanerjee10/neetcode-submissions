class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        left=0
        right=(left+x)//2
        res=float("-inf")
        while left<=right:
            mid=(left+right)//2
            val=mid*mid
            if val <=x:
                res=max(res,mid)
                left=mid+1
            else:
                right=mid-1
        return res
        