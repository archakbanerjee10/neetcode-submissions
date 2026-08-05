class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        if n==0:
            return 1
        elif n>0:
            for i in range(n):
                res*=x
        else:
            pos=abs(n)
            for i in range(pos):
                res=res/x
        return res
        