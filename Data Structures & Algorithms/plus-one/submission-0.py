class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for n in digits:
            num=num*10+n
        num+=1
        result=[]
        while num:
            dg=num%10
            result.append(dg)
            num//=10
        return result[::-1]

        