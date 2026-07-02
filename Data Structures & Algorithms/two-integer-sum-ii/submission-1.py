class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        my_dict={}
        for i in range(n):
            complement=target-numbers[i]
            if(complement in my_dict):
                return [int(my_dict[complement])+1,i+1]
            else:
                my_dict[numbers[i]]=i
            
        

        