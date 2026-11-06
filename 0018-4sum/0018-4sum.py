class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums)<4:
            return []
        
        nums.sort()
        res=[]

        n=len(nums)

        for i in range(0,n):
            #skipping duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=n-1
                while left<right:
                    total=nums[left]+nums[right]+nums[i]+nums[j]
                    if total==target:
                        res.append([nums[left],nums[right],nums[i],nums[j]])
                        left+=1
                        right-=1
                        #skipping duplicates 
                        while left<right and nums[left-1]==nums[left]:
                            left+=1
                        while left<right and nums[right+1]==nums[right]:
                            right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return res
        