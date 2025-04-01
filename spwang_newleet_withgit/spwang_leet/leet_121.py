class Solution:
    def maxProfit(self, prices):
        # dp = [0] * len(prices)
        # min_price = prices[0]
        # for i in range(1,len(prices)):
        #     dp[i] = max(dp[i-1],prices[i]-min_price)
        #     min_price = min(min_price,prices[i])
        # return dp[-1]

        cost,profit = float('inf'),0
        for price in prices:
            cost = min(cost,price)
            profit = max(profit,price-cost)
        return profit

test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))