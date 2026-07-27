class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #empty array
        if not prices:
            return 0

        #track the lowest prices 
        min_price = prices[0]

        # set max profit 
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price: #if the current price is low change min price
                min_price = prices[i]
            elif prices[i] - min_price > max_profit: # check if sell today is better than earlier profit
                max_profit = prices[i] - min_price
        return max_profit