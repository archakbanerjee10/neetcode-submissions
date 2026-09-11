class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=1:
            return 0
        mincost=[0,0]

        for i in range(2,len(cost)+1):

            nextcost=min(cost[i-1]+mincost[i-1],
            cost[i-2]+mincost[i-2])

            mincost.append(nextcost)
        
        return mincost[-1]
            
        