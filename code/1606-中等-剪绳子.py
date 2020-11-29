# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
# 思路：动态规划
# 长度为n，段数为m——max of {长度为n-1，段数为m-1；长度为n-2，段数为m-1；……；长度为m-1，段数为m-1}

def cuttingRope(n):
    formDict = {}
    for length in range(1,n+1):
        for block in range(1,length+1):
            if block == 1:
                formDict[(length,block)] = length
            elif block == length:
                formDict[(length,block)] = 1
            else:
                maxTmp = -1
                for lastLen in range(block-1,  length):
                    mulTmp = (length-lastLen) * formDict[(lastLen,block-1)]
                    if mulTmp > maxTmp:
                        maxTmp = mulTmp
                formDict[(length,block)] = maxTmp
    maxResult = -1
    # j为切的段数，从2开始
    for j in range(2, n+1):
        if formDict[(n,j)] > maxResult:
            maxResult = formDict[(n,j)]
    return maxResult

print(cuttingRope(2))
