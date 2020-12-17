def maxProfit(prices, fee):
    ############# 解法一：动态规划 #############
    # [0]没股票，[1]有股票
    dp    = [[0,0].copy() for _ in range(len(prices))]
    dp[0] = [0,-prices[0]]
    for today in range(1,len(prices)):
        dp[today][0] = max(dp[today-1][0], dp[today-1][1]+prices[today]-fee)
        dp[today][1] = max(dp[today-1][1], dp[today-1][0]-prices[today])
    return dp[-1][0]
