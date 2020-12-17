def maxProfit(prices):
    ############## 解法一：贪心 ##############
    vally = []
    peak  = []
    idx   = 0
    finding_vally = True
    while idx < (len(prices)-1):
        if finding_vally:
            if prices[idx] < prices[idx+1]:
                vally.append(idx)
                finding_vally = False
        else:
            if prices[idx] > prices[idx+1]:
                peak.append(idx)
                finding_vally = True
        idx += 1
    # 最后一天，如果还在找peak的话，那该日就是peak
    if not finding_vally:
        peak.append(idx)
    res = 0
    for i in range(len(peak)):
        res += (prices[peak[i]]-prices[vally[i]])
    return res
    # ############## 解法二：动态规划 ##############
    # dp    = [[0,0].copy() for _ in range(len(prices))]
    # dp[0] = [0,-prices[0]]
    # for today in range(1,len(prices)):
    #     dp[today][0] = max(dp[today-1][0], dp[today-1][1]+prices[today])
    #     dp[today][1] = max(dp[today-1][1], dp[today-1][0]-prices[today])
    # return dp[-1][0]