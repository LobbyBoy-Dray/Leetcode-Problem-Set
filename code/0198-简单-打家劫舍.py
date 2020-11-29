houseProfitStr  = "2 1 2 3"
houseProfitList = [int(i) for i in houseProfitStr.split(" ")]

# 动态规划
# 列表1，一栋一栋房子增加，最大的profit
# 列表2，一栋一栋房子增加，最大的profit实现时有没有抢最后一个房子(1-抢了，0-没抢)
N = len(houseProfitList)
maxProfit = [None]*N
LastHouse = [None]*N
for index in range(N):
    if index == 0:
        maxProfit[index] = houseProfitList[index]
        LastHouse[index] = True
    elif index == 1:
        maxProfit[index] = max(houseProfitList[0], houseProfitList[1])
        LastHouse[index] = True if maxProfit[index] == houseProfitList[1] else False
    else:
        if LastHouse[index-1] == False:
            maxProfit[index] = maxProfit[index-1] + houseProfitList[index]
            LastHouse[index] = True
        else:
            # 之前那个房子被抢了
            # 方案一：不抢房子index
            tmp1 = maxProfit[index-1]
            # 方案二：抢房子index，但房子index-1就不能抢了
            tmp2 = maxProfit[index-2] + houseProfitList[index]
            if tmp1 > tmp2:
                # 说明不抢房子index好
                maxProfit[index] = tmp1
                LastHouse[index] = False
            else:
                # 说明抢房子index好
                maxProfit[index] = tmp2
                LastHouse[index] = True
print(maxProfit[-1])
