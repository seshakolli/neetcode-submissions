class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        Map={}
        for i in range(0,len(prices)):
            for j in range(i,len(prices)):
                maxprofit=max(maxprofit,prices[j]-prices[i])
        return maxprofit
