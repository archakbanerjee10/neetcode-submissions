class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        result=0
        n=len(heights)
        for i in range(n):
            j=i+1
            while(j<n):
                a=min(heights[i],heights[j])
                b=j-i
                result=max(result,a*b)
                j+=1
        return result

        