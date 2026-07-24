class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(n+1):
            num=i
            count=0
            while num:
                if num%2 ==1:
                    count+=1
                num>>=1
            result.append(count)
        return result