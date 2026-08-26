class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(curr):
            # Base case: a valid permutation must contain all elements
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            # Explore every candidate for the next slot
            for num in nums:
                if num not in curr:  # Skip elements already in the current path
                    curr.append(num)
                    dfs(curr)
                    curr.pop()       # Backtrack to explore other choices
                    
        dfs([])
        return res