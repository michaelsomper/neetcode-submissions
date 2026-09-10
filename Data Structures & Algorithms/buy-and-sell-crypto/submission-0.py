class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buying_price = 101

        for price in prices:
            temp_profit = price - min_buying_price

            if temp_profit > profit:
                profit = temp_profit

            if price < min_buying_price:
                min_buying_price = price

        if profit > 0:
            return profit

        return 0

        
