class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i,curr,total):
            if  total==target :
                res.append(curr.copy())
                return 
            if not i < len(candidates) or total>target :
                return 

            #decision to include candidates[i]
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()

            #this piece of code helps us to not include any uplicate into our answer
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1

            #decision to not include candidates[i]
            dfs(i+1,curr,total)
        
        dfs(0,[],0)
        return res
