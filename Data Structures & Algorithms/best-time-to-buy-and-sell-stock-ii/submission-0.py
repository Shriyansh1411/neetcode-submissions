class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=1
        
        prevprofit=0
        profit=0
        while l<len(prices):
            prevprofit=prices[l]-prices[l-1]
            if prevprofit>0:
                profit=profit+prevprofit
            l+=1
        return profit
        