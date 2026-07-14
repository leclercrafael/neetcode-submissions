class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previous_min = prices[0]
        out = 0

        for i in range(1,len(prices)):
            
            previous_min = min(previous_min, prices[i-1])
            out = max(out, prices[i]-previous_min)

        return out
