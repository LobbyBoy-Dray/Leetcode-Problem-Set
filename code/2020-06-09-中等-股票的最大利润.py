# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
# 考点：动态规划

def maxProfit(stockPriceList):
    if stockPriceList == []:
        return 0
    dayNum        = len(stockPriceList)
    maxProfitList = [[None, None]] * dayNum         # maxProfit, minPrice —— 没有交易: 0,minPrice
    for day in range(dayNum):
        todayPrice = stockPriceList[day]
        if day == 0:
            maxProfitList[day][0] = 0
            maxProfitList[day][1] = todayPrice
        else:
            lastDayMaxProfit = maxProfitList[day-1][0]
            lastDayMinPrice  = maxProfitList[day-1][1]
            maxProfitList[day][1] = lastDayMinPrice if lastDayMinPrice < todayPrice else todayPrice     # 首先记录today的minPrice
            if lastDayMaxProfit == 0:                                                                   # 说明之前都没有交易
                if todayPrice > lastDayMinPrice:                                                        # 可以进行交易，先记录maxProfit
                    maxProfitList[day][0] = todayPrice - lastDayMinPrice                                
                else:                                                                                   # 仍然没有交易
                    maxProfitList[day][0] = 0
            else:                                                                                       # 说明之前有交易了
                possibleProfit = todayPrice - lastDayMinPrice                                           # 加入今天后可能的最大profit
                if possibleProfit > lastDayMaxProfit:
                    maxProfitList[day][0] = possibleProfit
                else:
                    maxProfitList[day][0] = lastDayMaxProfit
    return maxProfitList[-1][0]


stockPriceList1 = [7,1,5,3,6,4]         # 输出：5
stockPriceList2 = [7,6,4,3,1]           # 输出：0
stockPriceList3 = []                    # 输出：0

print(maxProfit(stockPriceList1))
print(maxProfit(stockPriceList2))
print(maxProfit(stockPriceList3))

