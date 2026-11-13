class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            diff = price - min_price

            if diff < 0:
                min_price = price
            else: # price >= min_price
                if max_profit < diff:
                    max_profit = diff
                
        return max_profit
