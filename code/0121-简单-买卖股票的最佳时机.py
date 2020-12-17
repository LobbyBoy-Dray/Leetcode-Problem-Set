def maxProfit(prices):
    if prices == []:
        return 0
    # ############## 解法一：动态规划 ##############
    # dp = [0] * len(prices)
    # for idx in range(1, len(prices)):
    #     min_i_1 = prices[idx-1] - dp[idx-1]
    #     min_i   = min(min_i_1, prices[idx])
    #     dp[idx] = -min_i + prices[idx]
    # return max(dp)
    ############## 解法二 ##############
    min_price  = float("inf")
    max_profit = 0
    for today in range(len(prices)):
        if prices[today] < min_price:
            min_price = prices[today]
        # 如果今天卖出的话……
        today_profit = prices[today] - min_price
        max_profit   = today_profit if today_profit > max_profit else max_profit
    return max_profit