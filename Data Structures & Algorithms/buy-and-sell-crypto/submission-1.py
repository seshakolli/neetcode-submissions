class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice= float('inf')
        best=0
        for i in prices:
            minPrice= min(minPrice,i)
            best= max(best, i-minPrice)
        return best