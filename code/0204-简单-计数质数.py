import math

def countPrimes(n):
    """
    埃氏筛法：
        - 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        - 筛掉2的倍数(自己不筛): 2 3 5 7 9 11 13 15
        - 筛掉3的倍数(自己不筛): 2 3 5 7 11 13——这里不用从2*3开始找，直接从3*3开始即可，因为2*3的那个数会被2的时候筛掉——筛p的倍数(自己不筛)，从p*p开始即可，p*(p+1)、p*(p+2)……
        - 筛掉4的倍数(自己不筛)：2 3 5 7 11 13——不用，因为第一个要筛的为4*4=16，已经大于15了，算法停止
    """
    if n < 2:
        return 0
    counter = 0
    sqrt_n  = math.floor(math.sqrt(n))
    nums    = list(range(n))
    for i in range(2, sqrt_n+1):
        if nums[i] is None:
            continue
        j = i * i
        while j < n:
            if nums[j] is not None:
                nums[j] = None
                counter += 1
            j += i
    return n - counter - 2