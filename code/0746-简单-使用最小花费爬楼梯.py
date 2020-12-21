def minCostClimbingStairs(cost):
    # ############ 解法一：DP，建构1 ############
    # # jio刚离开第i级阶梯时的最小花费
    # dp = [0]*len(cost)
    # # 初始化
    # dp[0] = cost[0]
    # dp[1] = cost[1]
    # # 状态转移
    # for i in range(2, len(dp)):
    #     dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    # # 返回结果
    # return min(dp[-1], dp[-2])
    # ############ 解法二：DP建构2 ############
    # # 达到第i级阶梯时的最小花费，楼顶相当于第n级，所以dp数组要大一个
    # dp = [0] * (len(cost)+1)
    # # 初始化
    # # 不需要，dp[0]和dp[1]都是0
    # # 状态转移
    # for i in range(2, len(dp)):
    #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    # # 返回
    # return dp[-1]
    ############ 解法三：递归 ############
    # 终点idx
    cache = dict()
    def helper(idx):
        if idx <=1:
            return 0
        if idx in cache:
            return cache[idx]
        tmp1 = helper(idx-1) + cost[idx-1]
        tmp2 = helper(idx-2) + cost[idx-2]
        tmp  = min(tmp1, tmp2)
        cache[idx] = tmp
        return tmp
    return helper(len(cost))