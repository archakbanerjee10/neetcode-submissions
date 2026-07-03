class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            a=-nums[i]
            j=i+1
            k=len(nums)-1
            while(j<k ):
                left=nums[j]
                right=nums[k]
                if(left+right==a):
                    result.append([-a,left,right])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                elif(left+right>a):
                    k-=1
                else:
                    j+=1
        return result



            



        