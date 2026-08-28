class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def dfs(i,curr):
            if i==len(nums):
                res.append(curr.copy())
                return 

            #decision of including nums[i]in the combination 
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            #decision of not including the nums[i]
            dfs(i+1,curr)
        dfs(0,[])
        return res 

            
        