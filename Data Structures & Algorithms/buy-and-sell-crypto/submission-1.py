class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        for i in range(n):
            j=i+1
            while(j<n):
                profit=max(profit,prices[j]-prices[i])
                j+=1
        return profit
            



        