class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        for i in range( len(temperatures)):
            j=i
            while (j<len(temperatures)):
                if(temperatures[j]>temperatures[i]):
                    result[i]=j-i
                    break
                j+=1
        return result
            

            

        