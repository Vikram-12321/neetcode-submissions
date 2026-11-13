class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 
        max_profit = 0

        for right in (range(1, len(prices))):
            diff = prices[right] - prices[left]

            ## starts at [0,1]
            ## prices[right] - prices[left] > max_profit, set that to max profit and left += 1 
            ## prices[left] > prices[right] => left +=1, continue. 
            ## prices[left] < prices[right] => right +=1 i.e. do nothing and continue.
            
            if diff > max_profit:
                max_profit = prices[right] - prices[left]
            
            elif diff < 0: ## prices[left] > prices[right]
                left += right - left

        return max_profit
