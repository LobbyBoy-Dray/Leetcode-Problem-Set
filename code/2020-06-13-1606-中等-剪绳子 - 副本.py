# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 思路：动态规划
# 长度为n，段数为m——max of {长度为n-1，段数为m-1；长度为n-2，段数为m-1；……；长度为m-1，段数为m-1}
import time

def cuttingRope(n):
    formDict = {}
    base     = (1e9+7)
    for length in range(1,n+1):
        for block in range(1,length+1):
            if block == 1:
                formDict[(length,block)] = (0,length)                           # 取0余length
            elif block == length:
                formDict[(length,block)] = (0,1)                                # 取0余1
            else:
                maxQuotient  = -1
                maxRemainder = -1
                for lastLen in range(block-1,  length):
                    quotient, remainder = formDict[(lastLen,block-1)]
                    tmp1                = quotient * (length-lastLen)
                    tmp2                = remainder * (length-lastLen)
                    # ======== 最费时间的两步 ========
                    # newQuotient         = tmp1 + tmp2 // base
                    # newRemainder        = tmp2 % base
                    # ================================
                    if (newQuotient > maxQuotient) or ((newQuotient == maxQuotient) and (newRemainder > maxRemainder)):
                        maxQuotient  = newQuotient
                        maxRemainder = newRemainder
                formDict[(length,block)] = (maxQuotient, maxRemainder)
    maxResultQuotient  = -1
    maxResultRemainder = -1
    # j为切的段数，从2开始
    for j in range(2, n+1):
        currQuotient, currRemainder = formDict[(n,j)]
        if (currQuotient > maxResultQuotient) or ((currQuotient == maxResultQuotient) and (currRemainder > maxResultRemainder)):
            maxResultQuotient  = currQuotient
            maxResultRemainder = currRemainder
    return int(maxResultRemainder)

print(cuttingRope(365))
