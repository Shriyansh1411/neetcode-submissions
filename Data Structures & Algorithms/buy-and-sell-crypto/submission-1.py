class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r= 0, 0 
        maxprofit=0
        while r<len(prices):
            buy=prices[l]
            sell=prices[r]
            if buy>sell:
                l=r
            else:
                maxprofit=max(maxprofit,sell-buy)
            r+=1
        return maxprofit    