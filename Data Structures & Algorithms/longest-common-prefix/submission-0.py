class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #lexicographically sort the given array
        strs.sort()

        #empty string to sdtore the result
        res=""
        i=0
        while i<len(strs[0]):
            if strs[0][i]!=strs[-1][i]:
                break
            else:
                res+=(strs[0][i])
            i+=1
            

        return res
            
        