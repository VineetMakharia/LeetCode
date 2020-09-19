class Solution:
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        lowest_price_seen = prices[0]
        profit = 0
        max_profit = 0
        for price in prices[1:]:
            if price<lowest_price_seen:
                lowest_price_seen = price
                continue
            else:
                profit = price - lowest_price_seen
                max_profit = max(max_profit,profit)
        return max_profit

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
print(obj.maxProfit([7,6,4,3,1]))