def maxProfit(k, prices):
    if prices==[]:
        return 0
    max_times = len(prices)//2
    dp        = [[([float("-inf")]*2).copy() for _ in range(max_times+1)].copy() for _ in range(len(prices))]
    # i：第i天
    # j：完成第j次交易
    # 0/1：手中没有/有股票
    for i in range(len(prices)):
        # index=i天，最多可以完成(i+1)//2笔交易，当然还有k的限制
        for j in range(min((i+1)//2,k)+1):
            if i==0:    # j必为0
                dp[0][0][0] = 0
                dp[0][0][1] = -prices[0]
            elif j==0:
                dp[i][0][0] = 0
                dp[i][0][1] = max(dp[i-1][0][0]-prices[i], dp[i-1][0][1])
            else:
                # 一次买入和卖出记为一次交易
                # 第i天，完成了j次交易，手中没有股票
                dp[i][j][0] = max(dp[i-1][j-1][1]+prices[i], dp[i-1][j][0])    # 第i-1天，完成了j-1次交易，手中有股票，第i天卖了/第i-1天，完成了j次交易，手中没有股票
                # 第i天，完成了j次交易，手中有股票
                dp[i][j][1] = max(dp[i-1][j][0]-prices[i], dp[i-1][j][1])      # 第i-1天，完成了j次交易，手中没有股票，第i天买了/第i-1天，完成了j次交易，手中有股票
    return max([l[0] for l in dp[-1]])