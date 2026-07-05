class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        i=0
        min_price=float('inf')
        while(i<n):
            if(prices[i]<min_price):
                min_price=prices[i]
            profit=max(profit,prices[i]-min_price)
            i+=1
        return profit
            
            



        